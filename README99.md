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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 646b0b78-c8f8-3bf3-a71b-f06739e8b67c | -4.4845 | -42.8631 | 2024-11-28 12:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 034766f8-d05a-37c9-a7d1-bf32196e5c4a | -6.1039 | -43.9824 | 2024-11-28 12:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1c97d6fb-81f9-3ad5-854e-0592febc016b | 1.4552 | -55.925 | 2024-11-28 12:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8719ad2e-2c77-3f3e-815a-ffb649d9ea0c | -3.4474 | -44.6039 | 2024-11-28 12:20:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 112.4 |
| dcaa7a4f-f7f7-35dd-97f8-9bce204ccdd1 | -4.4845 | -42.8631 | 2024-11-28 12:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e93d9d02-f5ee-373f-8326-c241ab2f50c2 | -4.6565 | -42.3811 | 2024-11-28 12:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 56729205-ad35-3a4f-85bc-b2cedeef77ae | -6.0853 | -43.9608 | 2024-11-28 12:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 69b32edd-0725-386b-959f-fac49edea0bc | -4.6753 | -42.3799 | 2024-11-28 12:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| cc1f24db-6ba8-341e-802d-0dccdd4f7a67 | -5.4546 | -43.2659 | 2024-11-28 12:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 6ac20a18-ed7a-3844-bbb3-6f005bb94bdc | -5.4548 | -43.2426 | 2024-11-28 12:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 234a90b2-08b5-30dc-b139-19e185f946d2 | -5.4546 | -43.2659 | 2024-11-28 12:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c4cee52c-0ced-39f2-afb9-b12c023c1841 | -4.6753 | -42.3799 | 2024-11-28 12:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 9b90e1cf-d70b-327c-b151-1d083839c6f8 | -6.1039 | -43.9824 | 2024-11-28 12:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| b514a4d3-c1ed-34ea-9871-635dfadd0cba | -4.6565 | -42.3811 | 2024-11-28 12:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 02a28600-1ac1-3833-9a2c-2d95102e4a7b | -6.0853 | -43.9608 | 2024-11-28 12:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 952e8f97-916e-3878-abc2-1b687f228aad | -1.44745 | -47.41316 | 2024-11-28 12:31:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 979fe1e3-bd37-3638-ba2a-6899762afd30 | -1.44911 | -47.40191 | 2024-11-28 12:31:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| bcc83295-148b-3823-b253-7138954f55c4 | -1.30151 | -46.01736 | 2024-11-28 12:31:00 | TERRA_M-T | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 90f0ff21-3c9a-395a-bd2c-807407d21999 | -1.30289 | -46.00786 | 2024-11-28 12:31:00 | TERRA_M-T | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c76e159e-a8e6-39c4-9ca9-322b40d58c2a | -1.89545 | -45.80342 | 2024-11-28 12:31:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 50c5ebb6-0f22-3d26-808b-a43faebc5cb4 | -1.20821 | -47.15786 | 2024-11-28 12:31:00 | TERRA_M-T | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d4025c49-3209-3feb-ab59-d50ef7b3997f | -0.98568 | -47.12984 | 2024-11-28 12:31:00 | TERRA_M-T | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 36e10ae9-f187-3b83-8940-42a4c84cd6fe | -1.11795 | -46.84922 | 2024-11-28 12:31:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ba9ad70d-83d0-31f4-bfc4-7d8d2066e006 | -5.35215 | -45.57569 | 2024-11-28 12:33:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 580d52bb-d341-3c65-8157-9b912d27634f | -4.7157 | -44.2328 | 2024-11-28 12:33:00 | TERRA_M-T | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 957a3835-67b4-3a44-8a9d-3d05d75346c4 | -6.5067 | -41.49467 | 2024-11-28 12:33:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 65d62d06-d240-39f7-a271-fee52753f043 | -3.46869 | -43.54025 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b0fdc34e-9a21-3364-821d-797a23ab086d | -3.65182 | -42.51403 | 2024-11-28 12:33:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 1f58690a-499b-32c2-87ec-cf5b6d7165c2 | -3.58294 | -44.7984 | 2024-11-28 12:33:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c16e26a0-6d41-3552-b445-01c8b2636420 | -6.12167 | -45.68637 | 2024-11-28 12:33:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9fac2c45-d2a4-35d3-82cc-8e3cf46a6485 | -4.24511 | -46.90617 | 2024-11-28 12:33:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ab099b8-f071-320a-8b5f-abf8a2a73fa9 | -4.94705 | -44.67298 | 2024-11-28 12:33:00 | TERRA_M-T | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f432fb79-a134-3970-b145-5c63b09ae472 | -3.92445 | -42.40432 | 2024-11-28 12:33:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 2c332443-1087-3561-9c36-2758c1941717 | -2.28583 | -47.91119 | 2024-11-28 12:33:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 68d9bed6-1012-3acc-af19-262eead834b2 | -5.52206 | -39.33195 | 2024-11-28 12:33:00 | TERRA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 1a8f1bf6-5caf-306d-9f10-3b1dcf585762 | -2.05308 | -47.12509 | 2024-11-28 12:33:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3928891a-8f37-3021-9fa0-595261fb9217 | -3.3347 | -44.41361 | 2024-11-28 12:33:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d3380036-1f08-3ec5-b381-3094d7378412 | -3.98727 | -45.64002 | 2024-11-28 12:33:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ff9c7251-025b-37df-9ee3-295e46391acc | -3.49271 | -41.96521 | 2024-11-28 12:33:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 42.8 |
| c6fc6015-518c-3c95-a832-8187845ded6f | -3.52352 | -44.94474 | 2024-11-28 12:33:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 21266389-ce88-3b2a-be6d-9b46b5cb81aa | -8.34576 | -43.93065 | 2024-11-28 12:33:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3cc4e412-8de2-342a-b0d8-e3bb635e30fb | -4.43756 | -46.34374 | 2024-11-28 12:33:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d316975d-bd3b-3f81-a94d-f1bafcfbee44 | -3.33176 | -45.50682 | 2024-11-28 12:33:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5d76750c-c762-3a82-a273-18fccf4170b0 | -5.14334 | -47.70455 | 2024-11-28 12:33:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 645e6cf2-f7a5-33d1-bc20-b9d3044ad991 | -2.85619 | -46.8779 | 2024-11-28 12:33:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 997fe0f2-bf03-3bfd-bdd5-a1cf64594510 | -4.27986 | -43.73667 | 2024-11-28 12:33:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0b966e2e-3da9-3296-99dc-f84087339d96 | -3.46689 | -46.16572 | 2024-11-28 12:33:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4ae361c1-ec51-3df3-9c0b-2bceac102f4a | -3.4379 | -42.45138 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 32.4 |
| d55d119d-81e1-3065-9fd5-2d27a0ff4cd6 | -3.17984 | -46.29742 | 2024-11-28 12:33:00 | TERRA_M-T | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 281158f5-80fb-3b83-977f-0b78f069ec9b | -3.33596 | -44.40482 | 2024-11-28 12:33:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 842a6339-e3d6-3cff-a1b6-e402053ad704 | -4.65985 | -44.17943 | 2024-11-28 12:33:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eb907a0e-6199-3cc3-a1bb-156db10eb3af | -5.11827 | -45.15527 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 97666b18-ae91-3255-a6aa-d892f0101de4 | -5.35343 | -45.56684 | 2024-11-28 12:33:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ab0393b-a09f-3460-849b-4410c9cdae87 | -3.69714 | -43.42498 | 2024-11-28 12:33:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 63ef4c8c-810a-39ea-a533-be49ad973f63 | -4.72658 | -43.25255 | 2024-11-28 12:33:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9cd8e76e-56d5-330f-a8cd-42b43e584a4a | -5.19051 | -43.55998 | 2024-11-28 12:33:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f831df92-0978-372c-8462-949551b9ec51 | -4.48595 | -42.86341 | 2024-11-28 12:33:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 77557d58-029f-3e82-8287-76e1bf649ece | -2.94922 | -42.33685 | 2024-11-28 12:33:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2ee832fa-8dbc-339a-b713-2c2bba3b5a67 | -3.96247 | -48.07469 | 2024-11-28 12:33:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| fc3e2e67-4638-3643-88b4-b2f3372eafa1 | -3.46999 | -43.53112 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 415db349-ab95-3f3c-a04c-32cc64edb307 | -8.14025 | -44.47395 | 2024-11-28 12:33:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0a8cd1e9-b284-3dac-bdb7-de4491abeb3f | -5.93265 | -43.7854 | 2024-11-28 12:33:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e378c226-21af-305d-abca-e52f8ac211e4 | -3.49433 | -42.18715 | 2024-11-28 12:33:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 130ed337-30db-3dd4-9fc4-5455dd149f54 | -6.0661 | -44.14609 | 2024-11-28 12:33:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| be698f20-d58e-3484-8cc7-0f8c8b1196a4 | -6.17608 | -42.02779 | 2024-11-28 12:33:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 13e5a199-4cd4-3087-a31a-d32a5c76b627 | -3.41287 | -42.18055 | 2024-11-28 12:33:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 45.5 |
| f80c9052-3447-32d1-9225-96b52c6ac40a | -7.69309 | -42.97664 | 2024-11-28 12:33:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 48a2b32e-7ac2-3dc5-af44-e91e29acb17b | -2.05496 | -47.17965 | 2024-11-28 12:33:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0d1d7c1f-edc2-3868-a8f7-54ecdb087f22 | -3.0662 | -42.80761 | 2024-11-28 12:33:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 887fead9-5ef5-3289-bf70-52e6de18c108 | -6.17453 | -42.03919 | 2024-11-28 12:33:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| d28aebef-0a17-3d3d-8b9a-be8d6a127475 | -3.49496 | -41.97146 | 2024-11-28 12:33:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| d3b47a7b-6c01-36be-a86a-61b43ed675d2 | -3.97249 | -48.07592 | 2024-11-28 12:33:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 390d16b8-87bf-3461-ba3a-f08f693987c4 | -7.32316 | -45.47199 | 2024-11-28 12:33:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 73c1631b-86ea-327b-b011-cd1aa6ba91e8 | -5.06913 | -44.98087 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 149f0e8e-2e59-35b1-a12d-bf9506375243 | -5.65204 | -40.79281 | 2024-11-28 12:33:00 | TERRA_M-T | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2bf36f9a-5bd5-3fbe-bf55-bae5ac3e70db | -2.91915 | -44.92118 | 2024-11-28 12:33:00 | TERRA_M-T | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| caa57034-60b4-38a4-896a-3ae9eca8ded4 | -6.15305 | -36.82206 | 2024-11-28 12:33:00 | TERRA_M-T | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 25e2a913-a23e-34c5-a41a-d9e88f0576e9 | -4.34769 | -43.78007 | 2024-11-28 12:33:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f016273b-148b-30f6-8b73-373766de40a6 | -5.14487 | -47.69414 | 2024-11-28 12:33:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ec71ae16-1ef9-33de-a400-2482ca1a66e3 | -3.33306 | -45.4979 | 2024-11-28 12:33:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f57aa305-07b6-3a68-8ab8-d990fe298e56 | -6.0888 | -44.88666 | 2024-11-28 12:33:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f1c2bc5f-3047-397c-8af9-f6467be2d870 | -3.38803 | -41.41237 | 2024-11-28 12:33:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d5034e8f-1f42-39b5-a43d-92e34503c4aa | -5.45414 | -43.25517 | 2024-11-28 12:33:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b1ec8dee-67e2-38ac-ada3-f4bbe3a9758d | -5.98483 | -45.35759 | 2024-11-28 12:33:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| a91a5dd0-9514-3065-97c0-44ea5ed16c2a | -4.77778 | -46.1016 | 2024-11-28 12:33:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 39dba222-ca7c-3c8b-a9e8-ea642309bf0f | -3.01411 | -45.66301 | 2024-11-28 12:33:00 | TERRA_M-T | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0719b502-a646-3768-96ff-b9593cd181eb | -3.00593 | -45.46943 | 2024-11-28 12:33:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 435fc4bc-d2bc-37eb-a301-00efec5111bf | -3.49287 | -42.1975 | 2024-11-28 12:33:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 157c6930-3394-3cac-bfc7-c0aafbbd06cb | -6.38692 | -39.14932 | 2024-11-28 12:33:00 | TERRA_M-T | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 86e2aef9-6257-3105-baec-85c01a629f6d | -3.02174 | -45.67329 | 2024-11-28 12:33:00 | TERRA_M-T | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 448fc4a9-8c90-3d1f-a2e9-312080d51f07 | -4.10062 | -42.4619 | 2024-11-28 12:33:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 07beb75e-b48b-39e6-be1a-7c73af9f289e | -4.34226 | -45.86136 | 2024-11-28 12:33:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9114404e-24f8-35c5-ac73-88bad565f3ca | -7.76518 | -43.79304 | 2024-11-28 12:33:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6053d8a1-e40e-30b1-8c06-53427e6bd28d | -3.4987 | -42.01568 | 2024-11-28 12:33:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 42.1 |
| fa37246c-758e-376b-abe2-029bfe2f0e60 | -4.15697 | -43.82439 | 2024-11-28 12:33:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4238990d-2a1f-354d-9291-a38957a5b217 | -3.65083 | -42.01013 | 2024-11-28 12:33:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| db27d3da-2ebf-3d43-b5dd-8bf15e050193 | -2.53691 | -47.32897 | 2024-11-28 12:33:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ab2e11b1-7597-33b6-bd75-1a99a822495c | -2.9398 | -42.33551 | 2024-11-28 12:33:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 613daa95-e207-35dc-9c54-f5130cf57ee5 | -3.0599 | -42.00047 | 2024-11-28 12:33:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4ef2702f-1fde-3c2b-bf33-ff361e68b2d9 | -4.47556 | -46.08656 | 2024-11-28 12:33:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README100.md)
