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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fc3f1c8-fb9f-31d6-b662-447e9d7ea2a7 | -10.64472 | -49.38093 | 2026-06-09 05:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 23697949-39d0-370e-a487-aa8dc4857855 | -11.55535 | -52.78648 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab7d54a8-2612-31cc-9434-3a7554de6a39 | -11.54906 | -52.78417 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 60a76469-3a2f-347e-ae0d-cbbd4949a206 | -6.5719 | -47.91755 | 2026-06-09 05:08:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee148c65-3d0d-3d26-86da-fd59ba66d913 | -11.26673 | -53.97194 | 2026-06-09 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7526ee84-b650-31ef-8b5d-b440909234f3 | -9.07956 | -50.6085 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40499467-1afe-393b-9b4d-6ae4ffee91e2 | -5.80707 | -43.78818 | 2026-06-09 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a4daf88-1129-3a91-9def-f038d9bf05ac | -9.31215 | -45.48572 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 307dba78-7c29-30b1-9115-d14e7114ebca | -10.42643 | -49.44476 | 2026-06-09 05:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 35e2f6e2-d0cb-3b5d-8ac3-c25ec39c28a2 | -9.20833 | -58.06391 | 2026-06-09 05:08:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2248136c-6f3d-36ab-b909-815572ba24f0 | -9.07587 | -50.60392 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1eb489e0-94bf-3a62-a06b-e25b8a029a05 | -10.77467 | -54.1023 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cd1eea5-e5e2-3ea2-8ecf-d4c8eb591df5 | -9.89061 | -47.85947 | 2026-06-09 05:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3346eae8-9ffe-3fed-aa28-8b408bf03075 | -10.64878 | -49.38657 | 2026-06-09 05:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f819255-7788-3dc2-9c21-051eee8d7acf | -9.21142 | -47.33436 | 2026-06-09 05:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18a014e9-c154-3857-b4ca-ab06703f3c7f | -8.97838 | -47.98423 | 2026-06-09 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6cbb811d-f44a-3162-b58d-a8a6087ffa14 | -11.53762 | -52.78241 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a216c348-0c8f-36e8-a74e-a3c68dcb810d | -11.54976 | -52.77942 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c35e7a52-aa63-39a7-a3e5-d428f58553a4 | -7.10072 | -46.50775 | 2026-06-09 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9d0c62e-1977-328b-a3c9-355e1af26625 | -9.30066 | -45.47983 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8bb06936-6fc9-3715-96b7-cf70ae7da993 | -8.72039 | -48.07688 | 2026-06-09 05:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fc36660-ac7f-3a64-8c58-68f3df5a8928 | -10.77528 | -54.09826 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4957fad-51f2-3cde-a02c-8e9096dac163 | -7.37685 | -49.85077 | 2026-06-09 05:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 167618f5-fdb6-3ae9-ab94-5351f8c4c2f1 | -10.38477 | -49.45158 | 2026-06-09 05:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3681bcf6-2fb5-37a6-bb89-0b21fc6ad6cb | -11.54074 | -52.78774 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7bdf2dd-e880-35f5-a49f-8e8647cb4a9b | -8.97373 | -47.9805 | 2026-06-09 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13a4d566-d3e9-3242-9a33-cae6ff3eb370 | -10.85409 | -53.74255 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94fe7547-9b16-3828-b5e4-e0c0ce8fc6b9 | -7.10024 | -46.51123 | 2026-06-09 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dc6a20f-434c-3223-bdff-688f7167e56b | -9.21172 | -58.06447 | 2026-06-09 05:08:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c04b79f5-7816-3eb4-8185-c1962ea967e9 | -11.55669 | -52.78529 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ea13cdf1-704e-3584-9e01-9e3db6546d68 | -9.33888 | -47.91002 | 2026-06-09 05:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6628375c-d278-3464-be73-5cc88ce41d59 | -12.05521 | -49.76693 | 2026-06-09 05:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4c833882-a5d7-3773-aba7-1cffc8f7aac5 | -5.83982 | -43.4917 | 2026-06-09 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3b7265c-4f51-32bb-b65e-0f5b8df6f4a8 | -9.31516 | -45.49299 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4410558-6a6d-3ea7-9bff-41b6c124a759 | -11.55357 | -52.77998 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ad84054-3a0e-3865-a48a-5b61dae6e131 | -11.54455 | -52.78835 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd3a93c3-76ba-3b44-b878-95abd5a3a898 | -9.46248 | -57.83628 | 2026-06-09 05:08:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1c91a26-2767-30b5-8924-bf63375602ea | -5.72983 | -49.09578 | 2026-06-09 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d70ad36-deef-392e-aefa-8321bdfa3312 | -10.14771 | -47.64949 | 2026-06-09 05:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd7ed87e-a08d-3b3a-b7cf-2991d06b15b7 | -9.08492 | -50.60114 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45e0ee23-afa2-346c-b00a-abae64c502e6 | -9.30669 | -45.48051 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc2aad25-17de-3bfa-b154-6d864d6de274 | -9.30973 | -45.48778 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ef92fd33-74fc-3c9a-9b9f-d5156e75dce8 | -6.64261 | -43.91323 | 2026-06-09 05:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7444e27-10b2-31f4-8914-37123e20057e | -10.85831 | -53.7389 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f294fd5-0822-3c1e-a1fc-59ed92016cc2 | -9.07698 | -50.59599 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59434173-862a-3024-ab1f-68b85b0caf7a | -9.3043 | -45.4826 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c71f8c2-a4d6-3ef3-b1f5-77747827500b | -7.10568 | -46.51207 | 2026-06-09 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86ccb74a-4b94-3fe0-bf79-c402ad96b615 | -11.64911 | -52.86105 | 2026-06-09 05:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f10fc91-af42-37bf-8a27-1ad6631ed748 | -10.84987 | -53.74619 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0602a1ef-99a3-3283-bef6-94a3dda1277c | -9.08011 | -50.60454 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2dde7c5d-62b3-313c-ab74-17baf10a2fb3 | -12.03263 | -47.80558 | 2026-06-09 05:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26ed934d-5878-3853-a663-e6ca7273f4d9 | -9.62433 | -49.02401 | 2026-06-09 05:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35824760-62aa-3111-8ffe-74f3a3165641 | -6.11832 | -53.08178 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bf0a437-7949-3a45-9ed8-823fd5d12679 | -11.54143 | -52.783 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 635c5b2b-35ef-30df-a29d-6d9c0f21c6cc | -10.85894 | -53.7347 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d40e8d46-857e-38b3-bca7-0f91686c17ea | -12.03306 | -47.8021 | 2026-06-09 05:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be6ae682-c391-3303-847c-172c4d6c1df9 | -9.24844 | -57.77203 | 2026-06-09 05:08:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5429bd8-0489-3e39-8797-e3a74d205f2a | -13.2597 | -44.388 | 2026-06-09 05:10:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| a3870c93-afe4-37e5-8a82-486d2d4391a0 | -12.44139 | -58.47062 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c52bb7d-226b-3e00-9145-9ef07998789d | -17.58517 | -46.65496 | 2026-06-09 05:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 15253b93-53d5-3c37-a133-611d4874014b | -11.61574 | -55.1815 | 2026-06-09 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8467e646-35c4-3446-975d-e777810ef36b | -11.96203 | -57.69647 | 2026-06-09 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fc6182b-a894-328c-89c2-aeabcc56f758 | -13.25453 | -44.40144 | 2026-06-09 05:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fe8e6e11-aa61-3937-babf-d5c32f9e21f9 | -13.25774 | -44.39573 | 2026-06-09 05:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0d5c278b-a06b-379a-8be9-38ca5b0e2a7b | -11.42698 | -58.70615 | 2026-06-09 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 389b0cef-0dc7-3b93-a7da-610c7b5c10cb | -11.47445 | -57.11129 | 2026-06-09 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e32b784-bd0b-30ca-ae91-c47604ef7360 | -14.29422 | -57.7084 | 2026-06-09 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2af53ed0-e728-371c-a1f0-36db8ea36e19 | -11.58952 | -58.50568 | 2026-06-09 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23cb52fa-b868-32bc-b964-8490ae67f1d1 | -11.47389 | -57.11479 | 2026-06-09 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad3553bc-8ef6-3719-9ec9-93b1d8722d66 | -12.85109 | -44.36854 | 2026-06-09 05:10:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 44be68f3-80c7-3eec-b4a0-02ff0002614b | -17.58566 | -46.64997 | 2026-06-09 05:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dee04c11-c09e-3001-8ff0-c7013490442d | -12.44198 | -58.467 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5ac63fc-d79a-349a-8ba0-3e8370dca436 | -11.61915 | -55.18203 | 2026-06-09 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbb17f1b-84b0-3c4d-a1ba-098e3c2a2784 | -11.62199 | -55.18631 | 2026-06-09 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bdb12ff-0f3e-38c8-8ed1-2ceec2cd511b | -11.79521 | -56.99454 | 2026-06-09 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab53864f-babc-3dc8-b236-6ec371a304a2 | -13.49362 | -56.5756 | 2026-06-09 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41cf3f3d-a05a-30fe-a621-cc69bad1e464 | -12.43468 | -58.46949 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d76945fa-1322-34ec-8404-e9581efb3f3a | -14.28701 | -57.53994 | 2026-06-09 05:10:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aee65b09-9298-30c2-b474-403121e6c6f6 | -12.46963 | -55.13573 | 2026-06-09 05:10:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36f3dc37-a682-3313-a376-591c9b1fa2f1 | -14.33073 | -58.4572 | 2026-06-09 05:10:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 76803524-3d73-3401-8cd7-d25762256ec4 | -11.89742 | -57.7803 | 2026-06-09 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ab55af4-7a7e-339b-bcc4-ddbd6a7b22ef | -11.42637 | -58.70987 | 2026-06-09 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baa879a5-6067-3163-a4fd-582cc14e20e2 | -12.67533 | -54.58258 | 2026-06-09 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237b07d4-9715-3db3-ae42-aac15cc56458 | -12.29753 | -57.38306 | 2026-06-09 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba3e05c8-095a-3591-9a0b-b658d393876a | -17.58615 | -46.64499 | 2026-06-09 05:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9dba7cc8-c10d-3019-bd65-6491ccde8d5a | -18.42241 | -54.54511 | 2026-06-09 05:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b374a01-58fd-3866-a1e2-91dae993d497 | -11.43038 | -58.70672 | 2026-06-09 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ba3bbfb-1ce6-3c94-b52b-2c2a88338d8a | -11.51462 | -56.11838 | 2026-06-09 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90a73b60-aa84-3c17-96bd-3161cf0eb73d | -15.1828 | -43.85665 | 2026-06-09 05:10:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1beef111-28ec-34b0-8348-5e693081740f | -11.57306 | -54.58503 | 2026-06-09 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a182b48-1561-3a2c-a593-6b58ad5fd7f5 | -11.96535 | -57.69703 | 2026-06-09 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d19ba644-a4e8-32cd-a06d-ab8025c3cdb3 | -14.31632 | -58.29278 | 2026-06-09 05:10:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ae04bb2-6aa7-3b8b-8c38-7d7272559dce | -13.25523 | -44.3952 | 2026-06-09 05:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cfc5bba5-8ed7-3c77-bb7c-e9548adccf7e | -12.43527 | -58.46587 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b4aab6e-20ba-3f3c-a87a-14900f65bfc8 | -17.81163 | -50.64355 | 2026-06-09 05:10:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4b4580e-a48d-3e75-8a98-d42f9a5a5859 | -11.47664 | -57.11884 | 2026-06-09 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7c5ae0-bd74-3626-aae1-4711435f61e1 | -11.90074 | -57.78085 | 2026-06-09 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b210d72f-4e72-3346-8f74-d4536c4036bb | -12.43408 | -58.4731 | 2026-06-09 05:10:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c6cd83e-0238-3d73-96ed-300bf2297d28 | -12.67121 | -54.58606 | 2026-06-09 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17321492-f320-38ef-b86c-5309e09940c9 | -11.47776 | -57.11182 | 2026-06-09 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
