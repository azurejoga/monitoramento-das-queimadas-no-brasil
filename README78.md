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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f7684d-c144-3e63-a084-895cd70efd1d | 1.602 | -55.7262 | 2025-10-27 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 1752a096-a5c5-337c-b968-9c76910c6071 | 1.657 | -55.686 | 2025-10-27 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7405616e-9a71-3922-8183-5a03b7106071 | -4.3879 | -43.3129 | 2025-10-27 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 7c67755a-4703-30bf-b454-f7af497191f1 | -6.4312 | -43.1411 | 2025-10-27 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 4d6c457d-8bb3-38ba-bfda-0a9d3fac0cba | -6.5414 | -41.6117 | 2025-10-27 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 121.8 |
| d9416e53-9722-35c3-9293-4b37d0c56f99 | -14.3168 | -51.7901 | 2025-10-27 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 8dcaa1e6-4573-3e03-a5cc-1bc95e0bfa9a | -7.8223 | -46.4664 | 2025-10-27 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 62f37c6d-53ac-3a9d-b2e5-cd555baa4e0d | -4.706 | -48.6328 | 2025-10-27 14:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 8328db64-25b6-35ee-b4a9-48441dd2e95d | -8.2682 | -46.892 | 2025-10-27 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| b55dacf8-75cc-3d59-9907-83a39429d0fc | -3.5834 | -43.5877 | 2025-10-27 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 423fbf70-d095-316d-9a95-6d281ccc98d0 | -4.0993 | -44.6183 | 2025-10-27 14:20:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 73990d76-3644-324d-beb8-ede4aac42d90 | -3.3447 | -42.9004 | 2025-10-27 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 74bb6a6d-f4ca-3d97-95fb-ad08b9429570 | -7.8225 | -46.444 | 2025-10-27 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b5ad99bf-9be3-3bf7-96c6-bec92d538b0d | -6.5417 | -41.5876 | 2025-10-27 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 163.1 |
| 3f830cc3-7741-39c3-b6d4-59d53ef96c3d | -7.2567 | -44.9851 | 2025-10-27 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d127bffd-558a-36af-9127-502c8d4b7db9 | -5.7758 | -42.9842 | 2025-10-27 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 179.7 |
| ecd572f9-bc0c-39d8-bd6a-3d9172274c41 | -4.8744 | -43.2595 | 2025-10-27 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 10dc70fe-407b-3c4f-9719-123a3c6ec067 | -14.3168 | -51.7901 | 2025-10-27 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| b2221079-bf7a-3ffd-88c5-0617ed490ea3 | -14.3599 | -51.5281 | 2025-10-27 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| a08c2fd4-728e-34c1-a013-2ddc3a43014e | -9.2467 | -45.5556 | 2025-10-27 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 717288d7-352a-34cc-814f-def2b752b8c4 | -6.4312 | -43.1411 | 2025-10-27 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 6188ee6c-b112-3780-af82-da99f25d3d7d | -9.549 | -46.9385 | 2025-10-27 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 171.8 |
| a0ad8829-f338-3a14-8cd6-216eb0ec9d41 | -8.287 | -46.8902 | 2025-10-27 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| c6849a04-ff42-3a73-9bf2-3f77ecc87094 | -4.3879 | -43.3129 | 2025-10-27 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 229.9 |
| 2710bd47-0d85-3815-a4df-32e035ed8d37 | -3.0577 | -44.3692 | 2025-10-27 14:30:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| b31bc49f-c80c-338a-898d-a8bf7c17d78c | -2.9961 | -41.6859 | 2025-10-27 14:30:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| d01ca4a5-e97b-325d-bcf2-83529da6f2b8 | -6.1737 | -42.5985 | 2025-10-27 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 66afbf9c-e2a0-3f4f-bf4e-d3cc75e1699f | -4.2035 | -42.95 | 2025-10-27 14:30:00 | GOES-19 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 45f7e7e7-b4eb-3d32-a8d0-bf9d5543d239 | -4.2457 | -42.2408 | 2025-10-27 14:30:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| b7ad7e2b-0c9a-3f55-8b90-1c865ff70efd | -6.986 | -39.103 | 2025-10-27 14:30:00 | GOES-19 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 31e81e80-c602-3252-8fb8-fb0bf6457eb1 | -4.0915 | -42.9329 | 2025-10-27 14:30:00 | GOES-19 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 23bd44ce-0e02-3c46-8a0a-e1a37cc70196 | -4.4602 | -43.6569 | 2025-10-27 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 3d720869-7df6-3e7f-a280-56c14f040eef | -4.0993 | -44.6183 | 2025-10-27 14:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| b9e3eb16-68b9-395f-b565-4242277b8124 | -3.6253 | -42.7933 | 2025-10-27 14:30:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 18557889-ce5f-3ce5-bf92-72ddd5eeb511 | -7.5429 | -46.2683 | 2025-10-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 179adcef-3002-3305-8c05-441a3a621a74 | -7.257 | -44.9623 | 2025-10-27 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 79141178-3130-30a9-854a-a46cf91a7f20 | -7.8228 | -46.4217 | 2025-10-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f14621cb-9a40-3525-ad0f-bdf370e461e6 | -6.5417 | -41.5876 | 2025-10-27 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 7e27c1b5-7f46-36db-89c2-3f9643a1ad8d | -6.2306 | -42.5463 | 2025-10-27 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 9632d198-77cf-32a8-8092-6461357cd81d | 1.657 | -55.686 | 2025-10-27 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 74412918-87b7-31d3-b0f3-4cdaf4589a2c | -18.2997 | -42.1438 | 2025-10-27 14:30:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.8 |
| b471442e-2b95-3eb4-b480-d80e94ca7de8 | -7.9252 | -45.6937 | 2025-10-27 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ff2f2205-81c6-3695-91f7-418288c2dc20 | -4.4618 | -43.4248 | 2025-10-27 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| d308c72a-b202-3873-9ba3-065d84009286 | -7.2379 | -44.9868 | 2025-10-27 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 3085b479-51c6-3217-82b6-9316a918664a | -6.6746 | -45.0357 | 2025-10-27 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5bfd04a4-44d7-37af-9436-6bb04450816d | -9.4745 | -46.8575 | 2025-10-27 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 26e1f86d-8737-32f1-ad04-56274cf9a726 | -4.4066 | -43.3118 | 2025-10-27 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 8d4c588d-92a7-35b9-bea9-506d1eb46610 | -3.5834 | -43.5877 | 2025-10-27 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| a20a6810-bc5c-3a06-b2c5-c33312852af8 | -6.1735 | -42.6221 | 2025-10-27 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 77a39f90-52eb-31aa-b8ac-fae08b4d0146 | -3.0148 | -41.6851 | 2025-10-27 14:30:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 151.1 |
| 1f7d9e8b-0d23-3ba7-a9f0-91eab83f711b | -7.6734 | -46.346 | 2025-10-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6da85c95-23f4-3afc-89f8-bdd1901b79ba | -6.5605 | -41.5859 | 2025-10-27 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 317.7 |
| 4a51045c-a2bb-3158-a697-c77469bd27f8 | -7.8223 | -46.4664 | 2025-10-27 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| aa3f45eb-24f9-3b34-a727-2261552d4912 | -8.0608 | -46.9558 | 2025-10-27 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0929a5da-b42c-35f4-9c5a-4dcaf160c51c | -7.822 | -46.4887 | 2025-10-27 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 8a5fb4ea-a4d8-35bd-93ef-39bc3b42d09d | -4.172 | -42.079 | 2025-10-27 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 822132f2-9321-3474-ac36-b3aaa99764ba | -4.9144 | -42.9295 | 2025-10-27 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ebe90c7b-2dd0-3373-b2b1-4bc003076e28 | -7.8159 | -45.3875 | 2025-10-27 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| f6c971da-466a-32cd-a425-5d7ca9a28d59 | -2.8971 | -42.8492 | 2025-10-27 14:30:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 2f10c06d-a82f-3a1c-84b4-316956fcfd3b | -14.3792 | -51.5255 | 2025-10-27 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 0bed8abc-ecf9-3639-88eb-c46d023b2811 | -8.3145 | -46.1734 | 2025-10-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fac9522d-b48c-3e82-b882-ccdf6b0cbda6 | -3.3261 | -42.8778 | 2025-10-27 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 052a94df-7ad6-3d50-b167-698236f3f2bc | -9.5679 | -46.9364 | 2025-10-27 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 336a0035-feee-333c-9344-3a2a316f02b9 | -8.2685 | -46.8698 | 2025-10-27 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5c1886d0-47d9-33d4-a729-325564c71175 | -7.8225 | -46.444 | 2025-10-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 892120e4-dda1-344d-8442-63a25b81af72 | -9.3083 | -45.207 | 2025-10-27 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| a200a48b-09fa-3de7-a2d2-19a7fddac235 | -8.4593 | -48.2159 | 2025-10-27 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 8ca76bdf-7919-3d53-bab8-0a5baaecb80a | -9.289 | -45.232 | 2025-10-27 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 789841c4-c591-334c-9da0-74a83d5cf9a8 | -7.0835 | -45.3865 | 2025-10-27 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3a5c8271-6add-304c-9c16-1998848cdc6d | -8.0971 | -47.0632 | 2025-10-27 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 37a17c3b-9509-358b-98a7-4650594065d1 | -7.5242 | -46.27 | 2025-10-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| f09a1ab9-e611-33fa-bca0-9a6d7ac62503 | -4.706 | -48.6328 | 2025-10-27 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| d6d3bc56-7ab5-3d7f-855f-c3409bc8f3af | -4.8953 | -42.9776 | 2025-10-27 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 63bdec73-2aef-3abb-bbac-2f40291ae83b | -8.0444 | -45.1606 | 2025-10-27 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 48885435-87d2-3ca0-8d15-598cd82021f8 | -9.308 | -45.2299 | 2025-10-27 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| f13ef7fc-e0de-37c1-b615-1837c280e165 | -7.0883 | -44.9319 | 2025-10-27 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b7f74afd-5029-30ef-97f9-50d050167c80 | -9.2464 | -45.5783 | 2025-10-27 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e0df5694-5d85-3bfe-a94b-3e60ec3a5e45 | -4.8744 | -43.2595 | 2025-10-27 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 38204834-3643-3b34-87bf-53ac425c579a | -4.9146 | -42.906 | 2025-10-27 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 917c632a-d240-372f-af66-65b131d160a1 | -5.9656 | -42.7574 | 2025-10-27 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 8fede15c-8c8e-3fe8-b2be-518d3f087a29 | -6.5864 | -42.6804 | 2025-10-27 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| c1d17b68-6478-34ec-987c-f12ba3225805 | -18.3199 | -42.1385 | 2025-10-27 14:30:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 287.1 |
| f76ecf94-8058-35f5-9134-3a2ba06f5edc | -14.781 | -44.9835 | 2025-10-27 14:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 9df211d6-8867-3f4f-a553-bf026cee11fe | -3.3448 | -42.877 | 2025-10-27 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| faa4b884-d222-3795-b527-36b4374df2f4 | -8.2682 | -46.892 | 2025-10-27 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 7c030c76-14e2-3b57-9d6f-037f2be9a259 | -6.9561 | -45.0118 | 2025-10-27 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b3bcbb88-2dc4-3fae-86f1-86efd82574e3 | -9.5676 | -46.9587 | 2025-10-27 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 206.9 |
| d51dd457-433a-3e73-b21a-90d28ad2f03a | -3.3447 | -42.9004 | 2025-10-27 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1efbfce3-deaf-320a-814c-4e35e513ba36 | -7.6922 | -46.3443 | 2025-10-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 4907e99c-3ec1-38e9-97d1-0ee7c4858a59 | -6.6746 | -45.0357 | 2025-10-27 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ae636718-96f2-35aa-8da5-a51fc2c0b13e | -10.0188 | -47.1528 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| f52f75ff-10d7-3f90-a2d6-9e5fec2fb420 | -8.2685 | -46.8698 | 2025-10-27 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ca62cc8b-2944-309d-8d2a-e8b10ea6b9b3 | -9.549 | -46.9385 | 2025-10-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 223.3 |
| f2c9ceb7-8565-3711-a896-1529fd6ed168 | -4.2035 | -42.95 | 2025-10-27 14:40:00 | GOES-19 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 734ae471-f0b1-32f1-bcb7-c322517c20dd | -6.4312 | -43.1411 | 2025-10-27 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 26408e10-3261-3c1b-a78a-4884bc43654b | -14.3168 | -51.7901 | 2025-10-27 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| f5ae3371-ef11-3382-8b8b-1115bfde42b9 | -7.9252 | -45.6937 | 2025-10-27 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 284b65ad-9452-3f8e-be93-7b8454ae35bd | -8.2873 | -46.868 | 2025-10-27 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| eba8fd7a-f7e9-3732-9720-79199b8223ce | 1.6387 | -55.6863 | 2025-10-27 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0b74f5b0-c71d-3941-b703-b1c8a0e49552 | -4.3879 | -43.3129 | 2025-10-27 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 185.2 |


[Clique aqui para ver as próximas entradas](README79.md)
