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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff7d99f2-c081-343b-96e1-4cc89095deb1 | -8.95734 | -63.61054 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d9df5411-01cd-374c-b5b8-78022ae49c91 | -8.95434 | -63.60518 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c68f9d0-6b75-3369-bc7a-ac926bb8a8ff | -8.80741 | -63.00489 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6f90ce1-ca38-33ec-89e6-6e1ac57cc339 | -8.77676 | -63.08396 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0550d869-5cdd-3ba2-aaf9-ce0cad45735d | -8.77603 | -63.08843 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c97ca7d9-5456-3fcb-bfed-2b8d05bbcae7 | -8.77589 | -62.83671 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| caeb65b0-dfee-3cff-b3d2-5fe3387678d8 | -8.77552 | -63.08101 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d3aa42a-5a4d-30eb-a1a0-cf44de1c8bdb | -8.77476 | -63.08546 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 973cf977-1592-3067-a5ac-55884b031562 | -8.77305 | -63.08338 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d142da0c-b925-35e7-b389-d3eeeae13e8b | -8.77224 | -62.83609 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c77dcc9-eff7-3c09-bb5c-a41c906b40d6 | -8.26231 | -62.99038 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c3145bc-1abf-32c8-a11c-e9ef75364623 | -8.24807 | -62.99498 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f499d71-bae6-3c18-a15d-d64155ecea4d | -8.24673 | -62.99234 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70a89241-dda2-3b1b-8e1a-8ab5a3b0255e | -8.24436 | -62.99434 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eb4c7ba-aa69-3954-92a4-fa338820d291 | -8.23391 | -62.96509 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbfd6254-efde-3abf-b705-cf12e16b03dc | -8.2302 | -62.96448 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f6e4ec-1568-3ef8-83dd-a2223de90f13 | -8.17986 | -62.83372 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc4d5ece-ace7-39ad-89cd-1dfb5a5028f8 | -8.17544 | -62.83747 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb7d1372-d641-349f-bede-76be3eae6a64 | -8.17471 | -62.84185 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 368cfb1d-d11a-3d7c-937c-e39ff9aa51f8 | -8.6562 | -63.65023 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18971d61-d07d-3264-a307-61afa54c247c | -8.63666 | -63.06635 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9a41989-a7e2-349b-a210-04ca9c03c825 | -8.62807 | -63.51392 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a40aa8a-7b41-37f2-8518-928eb0cf0847 | -8.62257 | -63.29091 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f09f8a95-9ad0-3e7f-b4fd-0bb13fa32e55 | -8.61882 | -63.29027 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bffe18ce-1f47-3a9a-bd20-988e44883623 | -8.60847 | -63.49128 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 129dd5a0-d030-3644-8c74-b5352a384105 | -8.60401 | -63.12497 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bff40729-8c3b-3426-82c6-75559836f6e7 | -8.6003 | -63.12432 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd9fe263-8122-3539-9141-e1c994e82b38 | -8.46526 | -62.65205 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2c93956-e11b-37ec-85b2-468f0711a090 | -8.46456 | -62.6563 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4f4317e-d12f-3f9e-8238-44841be533f8 | -8.46416 | -62.72648 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cb64829-a6a0-303b-8b4e-c002d32b6104 | -8.46385 | -62.66056 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1035825-2a65-304d-8a54-079230c9a532 | -8.46163 | -62.65144 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 520ee3de-20f4-39f4-bee0-65728921c5a2 | -8.46093 | -62.6557 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5257977c-cfcd-36a0-b353-9165fb8e7d67 | -8.46022 | -62.65996 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5757db4-a98f-33c3-9768-1e18b29c7114 | -8.45951 | -62.66421 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 903a92a7-ec48-3270-b722-76ddfdcbb7d4 | -8.45658 | -62.65934 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0aea2efe-9889-3626-b616-52dc2d60b7ac | -8.44211 | -63.44332 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b11a775b-1e48-3bf9-8768-b63f24c94421 | -8.39842 | -63.35634 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dac62d77-d2ef-3fd4-aa33-639782bf7735 | -8.39766 | -63.36099 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb75f40d-86a4-3284-8a2a-6122766ecdb8 | -8.39465 | -63.35568 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0da55392-9f08-3da6-831c-bab10d2bfb15 | -8.39388 | -63.36033 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10219a8b-86d0-3b52-9611-314dac61b816 | -8.39087 | -63.35503 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4b976e5-6679-3e31-ae9c-1771e0e8dfd3 | -8.3901 | -63.35967 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2cd85e85-a45a-36b5-beff-e86e15d36e19 | -8.38633 | -63.35902 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd2f4db3-26b6-39ca-abd8-062efab32ed7 | -9.95939 | -63.00152 | 2024-10-03 05:16:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8bd30c69-2d9b-39a2-a722-c12333a26fc4 | -9.72433 | -63.64471 | 2024-10-03 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb24e44-6864-30e1-913f-2994f607f450 | -9.69102 | -63.65795 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd296961-ea02-3076-81b0-8e85a920263d | -9.54523 | -63.14525 | 2024-10-03 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a669ff0-f74f-3115-b2d2-76c7a77cacde | -9.54081 | -63.14901 | 2024-10-03 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d173fb47-e5e8-3a26-b4d1-c5f2491a7c1f | -9.52369 | -63.61413 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0128ae94-367f-3fe2-8932-7b35a219030c | -9.50362 | -63.54906 | 2024-10-03 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99768b58-a5f2-3ebf-b03b-e401ff3f59b4 | -9.35543 | -63.80456 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a0956f8-c4aa-3f35-9cac-97d20db8f11b | -9.77965 | -63.93711 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d41c1653-3a22-3669-919d-d74e8f83afcb | -9.77884 | -63.94188 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 74c1c565-6b13-3ec4-b5bb-360f5b33a2f8 | -9.775 | -63.94124 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77f8180c-96f1-36eb-a316-088d7b1107a7 | -9.77419 | -63.94603 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ac3380b-98e1-31ca-8871-b78ccf963564 | -9.7685 | -64.28683 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b91be5b-6a9c-3e5c-b080-df3c0e2fe26b | -9.76813 | -64.28962 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99dd0b38-fd20-34ca-a2a3-982bd590a85e | -9.76421 | -64.28892 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 417a72dd-770e-386b-b2ff-2b397f9baf6b | -9.76371 | -64.29116 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d4c1c48-2e4a-3d3c-8744-053091afd53c | -9.76337 | -64.29396 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be0344a1-ac8d-3a4b-867c-f0c81b880d45 | -9.7603 | -64.28822 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c7986d6-4cdc-36fd-b015-3c56da05c5cb | -9.75945 | -64.29326 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5655dac-76d8-38eb-aa6d-21d6599da189 | -9.75554 | -64.29257 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2bfe287-cc7b-3ce7-80d1-5fe950f2cb47 | -9.75469 | -64.29762 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f2c62c4-c3e2-3309-97a0-0416bc0b4263 | -9.75162 | -64.29188 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2f9a7b6-1e3e-3954-b342-86956a8fcb40 | -9.75077 | -64.29693 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c93a68a4-31e4-3361-8566-dd8dd94015c3 | -9.72498 | -64.23521 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 774bfde0-194a-3ddc-8353-a7a551ba257b | -9.72411 | -64.24028 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41bb56e3-f737-3709-b761-6ad82a8c93d2 | -9.72108 | -64.2345 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f9ccb34-ea3d-3686-85e5-29d48a3bb58a | -9.7202 | -64.23962 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd203158-b10d-389b-acef-845822e2ac62 | -9.71717 | -64.2338 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a00a1df-3b1e-3955-85c3-1e756f53f857 | -9.7163 | -64.23893 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27ef17f4-9e5d-377c-b4fa-cabb07b5b23e | -9.71327 | -64.23312 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 771edf20-b484-3464-ac3d-457edb1a1309 | -9.71239 | -64.23823 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b22da49-4b19-3c41-8e9c-c51724e19e07 | -10.61801 | -64.05271 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 270a9621-b8cc-35f5-a83c-1b5e3257cdb7 | -10.6142 | -64.05199 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cc2a46b-743f-33e8-af4d-7888689fcd8a | -10.61341 | -64.05663 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ff4b220-57d6-3fd4-a883-35a007260a27 | -10.61038 | -64.05138 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 380b5ca9-0909-35ec-b7a7-a224d2ae7dc2 | -10.60959 | -64.05602 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a6fe487-da5d-34a4-bafb-b4fcf757e924 | -10.60575 | -64.05548 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eefb2a3e-6fee-3901-92c3-29ec268eb644 | -10.581 | -64.00017 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a839decf-01ce-3188-b916-74ba15cbe165 | -10.5802 | -64.00496 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a664e9eb-96a4-370d-83e3-efdc08baa897 | -10.57966 | -64.00215 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9fa42b1-4a16-3adf-af46-7e7fdce6c037 | -10.57721 | -63.99938 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcbcdc81-9b24-3ff1-bbea-ea3bc63298a5 | -10.57588 | -64.00135 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0f5329f-791d-3a7e-bd2b-d341189706e3 | -10.5748 | -64.01385 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9175b7e9-7304-32d1-b578-185e26ec0f94 | -10.57342 | -63.99863 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51fc6382-2106-327a-bc58-6fc1af90342a | -10.56963 | -63.99792 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d26c1655-4c27-3856-a436-26dbb53ba369 | -10.36776 | -64.08265 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54ffdff1-daee-36c7-a408-c98b2bd2d92c | -10.36392 | -64.08201 | 2024-10-03 05:16:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b38e12df-e3c4-3b29-adf7-6d439abfce0e | -9.54891 | -63.14586 | 2024-10-03 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bb230e1c-4be3-318c-ab08-a4e82905b8f8 | -9.54492 | -62.81047 | 2024-10-03 05:16:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9938fa9b-2aa6-336c-9dc9-72afea8e1e09 | -9.54449 | -63.14961 | 2024-10-03 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d83775e8-4f92-3920-b344-657bf170b18c | -9.51992 | -63.61344 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6480ebe3-4419-353d-947a-f10ac366d5c6 | -9.51065 | -62.92704 | 2024-10-03 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9eb7d334-5582-37fe-a314-de8691aa696c | -9.56074 | -64.25497 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0f1d59a-7cef-3a9d-9f1e-1f6d711334f2 | -9.56012 | -64.25733 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d13a1dc6-91f2-33dc-ae0c-f335c7320757 | -9.5562 | -64.25666 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a722eaee-9e83-3a6b-8ef9-bb6567d72b09 | -9.55598 | -64.25931 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README171.md)
