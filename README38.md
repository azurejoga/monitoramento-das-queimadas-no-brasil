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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68596942-6530-3c47-b8bd-9758d91c2e26 | -8.43881 | -43.86033 | 2026-09-20 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c3137fbc-42aa-3a17-89a5-6994047fa6bd | -5.84151 | -53.55272 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6b75472-343c-327e-b501-1dc08d3ac690 | -9.02119 | -51.42384 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ca75cd0-d183-362a-aaf4-fca9241d28c8 | -7.04654 | -42.09188 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc9de16b-472c-393e-8e87-24b25b79d681 | -7.37246 | -44.70974 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd46e15e-ec6e-3ffd-aa3e-ff57078bdd7c | -7.09847 | -42.08211 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4a21d58-2356-33ad-bc6f-febe1ed6da0e | -9.7362 | -46.08028 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78d0f77f-ba78-3eaa-86ba-ed1e942e438c | -8.26209 | -50.86043 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37aae2b8-753e-35af-90e7-9f1c64253810 | -11.08972 | -48.28876 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfe3d51f-6753-3f6c-83c4-72a2a6e9d925 | -11.32607 | -47.29099 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47cef467-b64a-39dc-a87f-b7afc45e9914 | -10.41751 | -48.90926 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4267fed8-7e4a-3a88-9f79-f0dd633dab0d | -4.68117 | -46.39833 | 2026-09-20 04:19:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7fbf4cc5-af7a-3abd-8ae5-c50e28014cdb | -11.00291 | -48.31324 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74aa2452-e86b-38ec-af41-1ac1e07b2514 | -8.36193 | -47.24908 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b208b4e7-dd97-3042-ae6a-7a77838fc0d4 | -11.48137 | -47.75875 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8388883-7e09-3867-8518-89b435166185 | -9.12683 | -45.72478 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ae6d5bf-48d2-3cee-8185-3935c81a6071 | -9.73091 | -46.08883 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6745711c-a306-3483-b805-2f05ddc94b7d | -5.83197 | -44.13137 | 2026-09-20 04:19:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a635397-5315-34ce-9d48-25e3e48e8709 | -5.40709 | -44.27327 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e47e313-8484-3dc9-92a5-d1c1308a3cd9 | -8.1743 | -54.76705 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e101de10-302c-39c5-a315-d1798e6e4a59 | -5.84545 | -53.53157 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee54abb3-c434-3818-8067-509eaac3d2c1 | -5.22248 | -47.57391 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8b7b8c4-ff39-35fc-abb7-85ce804e148f | -6.20321 | -47.52126 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b35fa15b-556b-32f3-8035-d1cb055b1d2a | -6.25307 | -41.69397 | 2026-09-20 04:19:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70549619-f432-3853-a6e3-853242074bd8 | -2.97133 | -54.7687 | 2026-09-20 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c21cf1ad-72d6-3dae-8475-b2d6fb31429a | -7.74216 | -46.70995 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2662d1a1-e86e-30c1-a36c-5c5b6fb337b6 | -7.54837 | -45.43074 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 26f0ac0a-1d7f-3627-9dbf-99fbcf485894 | -7.34489 | -44.47582 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33393354-e054-355f-b463-234eee48dcda | -6.31502 | -47.62796 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b9c6225-538a-3c2b-a68f-416be032a4f5 | -10.77995 | -46.33411 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ed1d01e2-5777-3e07-9b86-9a17474417c4 | -7.28086 | -45.55179 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e328ada-8039-3709-bd3b-be7b08f22ab8 | -6.29974 | -47.61263 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f84d8411-3906-3c4a-bad5-4187113ca1a1 | -10.31872 | -50.21574 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 830d4bf5-8848-34fa-9f71-e4a060825d63 | -10.32172 | -45.32769 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b1a109f-ebe1-3058-96af-b70a99a91c5f | -6.36463 | -43.36214 | 2026-09-20 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5a6bd09-c748-3a48-96a2-62df02fa094b | -9.9444 | -45.54731 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c930c707-4b0e-33d2-a270-9bc21d0dffa0 | -10.32124 | -50.21515 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b7326950-ab92-351d-b5f6-e01feca10abe | -10.84132 | -50.93395 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1b45951f-004a-3de4-a606-d42c58fc13aa | -9.2195 | -43.18258 | 2026-09-20 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d03a91f3-72e1-3951-b20b-dcabdf226dd7 | -5.6688 | -45.30262 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5a1fd48-59f7-37a1-9bc1-9859a6a1c5ed | -11.03934 | -48.30392 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b3c4dd-ec0d-3dc1-9e18-77fbe79ba957 | -11.46007 | -47.64435 | 2026-09-20 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7539e382-361b-3fa9-93e7-fe3be071c7d2 | -9.82272 | -46.43304 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9d115f0-f494-3d43-920d-e8e44244fe69 | -10.27857 | -50.25713 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 18cfdcdb-b22f-328d-b89d-e07924ad1644 | -5.83808 | -47.78838 | 2026-09-20 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43bbe403-317d-35e6-84c0-369644c46d27 | -7.29612 | -46.73937 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8acb061e-4581-3c35-a342-28de69279672 | -7.60125 | -55.7104 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2542273b-ccb5-3a71-a05c-9d8cf957e82b | -9.80944 | -48.32627 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11e4af26-4747-35f7-a25e-64948b002da5 | -8.38761 | -47.19025 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6af97c9c-f01b-3c28-837c-7f96ab4498cf | -6.38958 | -51.68087 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02688d5e-15ad-31ba-8d77-f33d6783061d | -5.82632 | -47.77711 | 2026-09-20 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfcc6536-b7b8-36f4-b129-4aac5b2fde86 | -11.31825 | -47.2894 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 42dfada5-1757-3fed-a2fe-0ad939cc9d10 | -11.47305 | -45.33851 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce21b91c-1201-33c6-bc97-25f9f2aaa330 | -10.31772 | -50.22109 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| d8c2bf26-e8c6-3f8d-9256-258190af2aba | -10.27372 | -50.2562 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 19857ba2-dd5a-350d-aab9-12dfdba44323 | -8.67782 | -45.41987 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acbce0fa-15a8-392f-919e-bc2d7c8b5066 | -8.76925 | -48.69989 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93bbbb5e-21dd-3ade-98cc-441ff4231ddd | -8.42818 | -46.86267 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6b2c394-d2d7-3a9d-9ad8-dd83894f85b9 | -10.47736 | -46.29469 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee899c46-eedf-3380-886d-26a2a745794d | -5.28082 | -44.26405 | 2026-09-20 04:19:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61f66b8f-a389-3291-a1a5-944274e98063 | -6.6187 | -50.0643 | 2026-09-20 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bf7dae6-54b0-3c89-a4d0-bd7b972a9982 | -8.04881 | -46.24934 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d5c3c71c-3b4b-3efe-9f55-dee283a984c8 | -8.61712 | -54.60765 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a6d0036-4f0d-3837-aedc-5f1e5d93f236 | -3.44698 | -50.59884 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a9f96f2-73c5-3090-832e-2f0b230e1058 | -8.61376 | -54.58961 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e96af825-2bda-3186-b054-69626dcb305a | -7.88357 | -44.84806 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 37a5d77d-41bd-3ca2-9f72-6fbf431f6e2a | -8.65962 | -45.43886 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7d838a-6e10-3bcc-a152-52082fd48a39 | -8.37586 | -45.63805 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef091484-9cf5-3ac9-8b23-868084e229c2 | -9.66886 | -54.31718 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b6d55e4-97fd-35f2-9ca8-b0a30857923a | -8.76827 | -44.25401 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9725aefa-5b65-3440-acf6-e37a43253c19 | -3.45194 | -50.60347 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8de515f2-a342-3f20-be6b-60c7973ca2d0 | -11.49004 | -47.75671 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4de52c82-870e-3043-8863-ec90f5ece7ee | -8.76728 | -48.67371 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2cb40ca0-87b0-308e-a23b-cdd53720ce21 | -7.43129 | -44.73978 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c82c695-b010-3e12-b354-6c5d8a04a208 | -8.17642 | -54.76751 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c0b1026-dfa5-387b-a510-293b3395a310 | -11.33999 | -47.3508 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c2615a4-64ed-3db0-b923-2c60b36c3e08 | -3.45567 | -50.61547 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22068bbe-2fdb-3513-919b-3eca15906200 | -10.33947 | -45.30973 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaffd01f-d884-34b5-96e2-a402e1e3ab4e | -6.20441 | -47.35919 | 2026-09-20 04:19:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79077abe-1cb9-3ef3-b8e2-065026bca4e9 | -11.45726 | -45.38951 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a0d9109-d276-3e40-9caf-5381050f9228 | -8.7718 | -45.85884 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94cedd22-2716-305d-b69e-92a46c890b1d | -9.69244 | -48.318 | 2026-09-20 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f85c6a9d-9778-31c8-a9f6-0acab7403170 | -11.15351 | -42.81536 | 2026-09-20 04:19:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d779cde-d1e1-340a-93ad-ca0c9609c678 | -6.19639 | -45.33404 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ede13b26-d935-3855-9377-9ff0dd0165db | -3.89286 | -49.06677 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1fa80be0-91f7-3c69-bdcb-e33a789f07f8 | -5.9318 | -35.61975 | 2026-09-20 04:19:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e0e49809-6964-3d06-ae51-9b68a6ee4bf8 | -9.89887 | -46.52613 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fc632cb-3ba0-3cf3-b933-f5aa59f62a61 | -8.42535 | -54.72688 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53f7017c-65f5-3ca8-bbf9-ba93395f57be | -10.39619 | -48.90076 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ca96136-20f1-3c15-879b-11ffcfaf3a00 | -7.49289 | -46.70928 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d506a3c4-3488-3cff-be85-35638ceccb86 | -8.17764 | -54.74947 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25b02662-1e62-3f26-bc19-c20d27ba1a72 | -6.31068 | -47.6272 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47e5e929-7149-36fa-a686-b165dd154cd2 | -6.98855 | -43.36979 | 2026-09-20 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8210dcef-f964-3393-9fc9-2d8aa98e485a | -8.43528 | -46.86117 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c59c2467-6011-3b36-98d8-e83ffb5ea407 | -7.5941 | -46.14384 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 233d6891-da6b-3273-819b-d5b1daf2fa55 | -8.17323 | -54.73624 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b6bbcda8-8814-3e89-bd3a-769ff292029d | -6.20463 | -45.35398 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ca7d57a-b0df-3886-8c51-60a5336d4462 | -6.02179 | -45.4087 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca1efde9-419c-3734-a9f9-122569f75ae3 | -7.44208 | -44.7415 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fefd1832-1aad-3356-8c3f-79dec5609332 | -6.19716 | -45.32948 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
