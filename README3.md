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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9889cf38-0100-3aad-be59-f0dc653fed20 | -5.7376 | -45.1533 | 2026-10-08 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 98f93b7a-db1d-39d7-9484-7e8a07e0060d | -16.8948 | -40.8938 | 2026-10-08 00:10:00 | GOES-19 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| 22d00172-e382-3aed-b371-bdabb67c0ea6 | -16.8835 | -40.5915 | 2026-10-08 00:10:00 | GOES-19 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| e4f41347-d3ea-3dfe-bfa8-ab9b89cb04f8 | -6.6317 | -43.73 | 2026-10-08 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 247.7 |
| b5705c3e-650d-3264-921c-d39637b96dc2 | -3.1114 | -53.7839 | 2026-10-08 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 9128e081-0881-3842-b2e8-aafcdfd33b86 | -3.1792 | -50.4551 | 2026-10-08 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a4dc9039-f678-3252-84ad-cb7a8cc93d80 | -2.5537 | -56.1649 | 2026-10-08 00:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 45ff549b-03c4-3914-85c2-e052d26a0f72 | -9.0406 | -65.9401 | 2026-10-08 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a0a121d9-9940-349e-bc41-e15304ef443d | -3.1697 | -58.6437 | 2026-10-08 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7eaefa6a-85fa-3e5b-9cc0-860a7061b7bf | -3.1601 | -50.6021 | 2026-10-08 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 26dbf51d-917f-34df-8bf6-a38a86d0c33d | -5.9587 | -55.3448 | 2026-10-08 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 2560155c-3de5-3063-b046-fe2dfcf9ad73 | -6.15 | -39.4409 | 2026-10-08 00:10:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 99be2be6-478d-33fa-aae4-4e5b890092bb | -9.4935 | -64.3706 | 2026-10-08 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4ba1ab65-dae9-3585-96bd-137388c5aa21 | -2.798 | -54.0933 | 2026-10-08 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2d4f1057-63c0-3a84-b6d1-cd6c0bc099a5 | -3.1607 | -50.4556 | 2026-10-08 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6a6f8ec8-419e-3d84-a915-190667fad269 | -3.1101 | -54.1661 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 8e078fd8-3368-39b3-80ac-d9d2bdf7912c | -3.1284 | -54.1857 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 36bfd200-e7fa-3cb1-9215-eca9fc362270 | -6.2342 | -52.8685 | 2026-10-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 2a6bf723-9dae-3add-95dc-d64bb9e9121c | -8.3882 | -46.3006 | 2026-10-08 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 058237be-6299-309b-9434-4e86b1dd3e64 | -4.1176 | -59.8888 | 2026-10-08 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 250f98f8-d173-303f-aacc-951f03795e4a | -6.6129 | -43.7317 | 2026-10-08 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 3e269af0-f429-3926-b6c3-6a265fb3d085 | -9.8261 | -44.7781 | 2026-10-08 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 1dac56d9-2517-3121-8dcb-71ea4bcdee96 | -6.2343 | -52.848 | 2026-10-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 8776d8fe-d1dc-368e-90f4-fe67a8d5d4af | -6.2527 | -52.8675 | 2026-10-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 1e76bc7d-cf91-39fd-838d-c100d9cc0d87 | -3.8566 | -55.9967 | 2026-10-08 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 494fe839-4fc5-390d-95c8-e3339a5f5bb7 | -9.4936 | -64.3518 | 2026-10-08 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 5017c641-66b9-3f1c-9a9c-4e6fa405531d | -3.8567 | -55.9769 | 2026-10-08 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 5f4dcad1-9a2d-34b6-8242-c2403b920cdf | -2.8712 | -54.192 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 08c73c4f-73f7-360c-9151-15a0aeeb8907 | -2.7981 | -54.0732 | 2026-10-08 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 42faaac0-384f-3498-afbc-dec0fc1eb143 | -3.5515 | -59.4807 | 2026-10-08 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 8e4afd96-d7af-3edf-a083-385a123e41c4 | -6.2158 | -52.849 | 2026-10-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 3e86300f-71b3-360c-b8a1-c0304958780e | -3.1879 | -58.6433 | 2026-10-08 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ecf225ca-ece3-3b04-8237-0f38f57275cc | -3.1786 | -50.6016 | 2026-10-08 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3fbe4395-ea25-335a-bf03-32e5f136c34f | -3.0914 | -54.2669 | 2026-10-08 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2272e111-f6d7-3883-99f5-ec26cd77b1cf | -3.0 | -54.17 | 2026-10-08 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6e1891-e263-3d4c-9e05-7bc1567477c2 | -6.61 | -43.74 | 2026-10-08 00:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd4ad4f2-e8ef-3fcb-9bd2-e513f5c87219 | -3.59 | -54.67 | 2026-10-08 00:15:00 | MSG-03 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd53b546-5d95-396b-9025-3a0f1e6cf692 | -6.64 | -43.75 | 2026-10-08 00:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa6d172-3afc-35a6-a120-ab3178b1d632 | -3.56 | -54.67 | 2026-10-08 00:15:00 | MSG-03 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd9c5d66-9ae2-3407-9948-3d884c1d2e17 | -3.0 | -54.11 | 2026-10-08 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd5b65d-3a8a-34d0-9b4d-f476922a0317 | -3.29 | -54.07 | 2026-10-08 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8ac5ae-c972-3262-87f7-a481a9f1224c | -3.02 | -54.11 | 2026-10-08 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68585319-7bac-3679-b485-4c5550acbbde | -3.0 | -54.04 | 2026-10-08 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6891068-5762-3545-a0da-d1e4c0494e85 | -3.02 | -54.05 | 2026-10-08 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef6d9740-8781-37ed-a144-ae013531b2af | -3.26 | -54.07 | 2026-10-08 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1db7b198-7406-3e01-ac60-dc410d946ec4 | -3.5698 | -59.4803 | 2026-10-08 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 69eff3d1-16cd-3d6a-97ff-8cf3696a9081 | -3.1786 | -50.6016 | 2026-10-08 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 010c9f5f-acff-3d05-aac4-b17f5c1cdee5 | -3.8383 | -55.9774 | 2026-10-08 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b444f97a-7898-36ee-b209-cc015962b418 | -7.2179 | -55.1817 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 318359a8-3b4f-3a65-93ce-6f3a8d53333a | -8.7039 | -45.1832 | 2026-10-08 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 14c8b316-6fd4-38b5-ba99-8f19d8bb39c2 | -7.0063 | -59.1416 | 2026-10-08 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 88b6b672-3e35-3510-874c-f95a94fea41c | -4.3473 | -43.779 | 2026-10-08 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a94a33e1-e5e9-378a-90aa-c2d742e0bb0b | -9.4935 | -64.3706 | 2026-10-08 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f6ed6de0-ffc8-3dca-a8cd-53a481ff49d9 | -5.7117 | -53.4862 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 199.9 |
| 054b0728-64a0-3dd1-954c-643e3f4b9c17 | -4.0628 | -59.8328 | 2026-10-08 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 93ca09ae-f911-3ee4-9606-315484f886ca | -16.8835 | -40.5915 | 2026-10-08 00:20:00 | GOES-19 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.0 |
| 3d708f42-dac4-3b15-a671-64f8a7541153 | -3.8005 | -41.6468 | 2026-10-08 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 9ad4e61b-3b2f-3997-ab45-dc7ca2b90f4c | -3.1601 | -50.6021 | 2026-10-08 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 83b96945-d8cc-327b-999b-ec7d06849546 | -2.7981 | -54.0732 | 2026-10-08 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a97f7975-9189-310d-8c55-a8ef770b4de0 | -9.475 | -64.3525 | 2026-10-08 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.1 |
| ef907e3d-126a-38f5-9925-8704c447fc23 | -5.7498 | -41.7534 | 2026-10-08 00:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| a09f96c8-3668-3874-9d2b-f011dded22c1 | -1.1094 | -54.1601 | 2026-10-08 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 0390787d-ee28-39af-8956-2a9a8f391570 | -3.5515 | -59.4807 | 2026-10-08 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9d92ae28-5fac-365e-8fcc-be433a08e056 | -16.8634 | -40.5966 | 2026-10-08 00:20:00 | GOES-19 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 164.2 |
| b9909a4a-e003-3793-9afa-9a553a8caad5 | -4.1176 | -59.8888 | 2026-10-08 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 663b978a-f494-3c46-9a01-3191ba5173ec | -5.6931 | -53.5073 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 70887b82-20be-3ce4-b1a0-d8bac250883c | -2.117 | -54.8067 | 2026-10-08 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| df944793-e720-3116-a25e-a072de7f36e3 | -5.9587 | -55.3448 | 2026-10-08 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bf1cf53e-8827-35bb-8a07-76ed6e270b50 | -2.7613 | -54.0941 | 2026-10-08 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c556b613-1aa3-3f81-a796-bdc181db9db6 | -8.7417 | -45.1791 | 2026-10-08 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 0dc9d1b8-1a9e-39fa-abd1-b12199741a33 | -7.4443 | -63.5401 | 2026-10-08 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9b1a17b8-730f-36b5-bbd6-04444c46cd10 | -10.4527 | -47.2801 | 2026-10-08 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8f56604b-fa86-37ec-a957-32c6002ef036 | -3.0917 | -54.1867 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 53170fa6-ca65-3f69-b7e0-902246b1ee74 | -4.0811 | -59.8514 | 2026-10-08 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 375b5718-4747-306d-8f37-0a7d4736de16 | -1.5302 | -54.8151 | 2026-10-08 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 19dbd136-9024-3d1a-8537-7ee450e7bd43 | -7.218 | -55.1617 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 56e33f27-ed5f-3b05-a58c-b63e23e7f17b | -2.7612 | -54.1142 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 3cc8343c-d1ef-3912-8f16-cf0b206a5986 | -3.0913 | -54.287 | 2026-10-08 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 8c36a04e-a4c3-3973-8be9-00d0c40056de | -5.6932 | -53.487 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 212.2 |
| 93b4a735-e39b-3fd4-bfee-c3c8c2b0ab3a | -3.8567 | -55.9769 | 2026-10-08 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| d42ee614-a2b3-3672-8860-96b3fe044f0e | -2.1629 | -59.2361 | 2026-10-08 00:20:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| bb73226e-320b-3b08-b9bb-3e1247a47bd0 | -2.572 | -56.1646 | 2026-10-08 00:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 7fa8a70e-d206-3f75-b622-5e5b4212d33e | -10.434 | -47.2601 | 2026-10-08 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5468a963-8340-356d-a2ff-ec7c87e676c4 | -4.2953 | -49.1021 | 2026-10-08 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1319fd34-20b9-3c09-afff-f4e4dc545c59 | -6.2343 | -52.848 | 2026-10-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 344961da-1384-32a8-b759-38d54b837dd5 | -6.6317 | -43.73 | 2026-10-08 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| a4c62416-d4a3-3725-8ff5-3f7291312d23 | -7.8478 | -49.285 | 2026-10-08 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| bda89273-601e-3b5d-8021-d66dd04ad6d6 | -3.1285 | -54.1657 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 1361e619-cffc-3bb5-a7eb-b086e46f0803 | -2.8575 | -59.1107 | 2026-10-08 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| fe759cbf-bd60-3d61-b528-83164c688e63 | -6.6129 | -43.7317 | 2026-10-08 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 44651d27-3d0e-3e8e-ac53-1c597e36ba11 | -3.1114 | -53.7839 | 2026-10-08 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| d8fdab15-0050-3802-9c2f-d6c97ceffad3 | -9.4749 | -64.3713 | 2026-10-08 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 78b0dd91-f920-36a8-ba45-4ff6176e2fe5 | -10.0255 | -36.351 | 2026-10-08 00:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 19310c09-3dd9-3491-babc-11a88f0bf4cc | -4.1176 | -59.8697 | 2026-10-08 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| dff8e096-09ae-3018-9c5c-1d13e7da72d0 | -5.7376 | -45.1533 | 2026-10-08 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 3a6fec33-0bbc-338b-a642-94f7765c4a68 | -8.7225 | -45.204 | 2026-10-08 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b36ea49d-0523-3b92-8144-887cc7e7026a | -3.5865 | -54.5742 | 2026-10-08 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f491ca45-70ad-3b51-a6bd-d785252bf0cd | -8.7228 | -45.1812 | 2026-10-08 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 236.9 |
| dcfd5624-e00e-3b0f-9cf5-b0859079ebd7 | -3.073 | -54.2874 | 2026-10-08 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 1556c76c-443d-318b-9075-2aad57d08662 | -3.2313 | -46.9596 | 2026-10-08 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |


[Clique aqui para ver as próximas entradas](README4.md)
