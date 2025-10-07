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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 657bcf56-0289-3fc5-8e10-7acdc7a7e12d | -12.9101 | -54.7558 | 2025-10-07 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3ade9a9a-322d-3ce9-8689-f091946b7210 | -8.5599 | -44.6494 | 2025-10-07 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 9eaf90d0-099c-3766-b3e7-19ad36d71bf9 | -10.3247 | -46.9612 | 2025-10-07 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 90d82f86-fcea-3210-af07-f225a1c6f280 | -14.8835 | -51.4346 | 2025-10-07 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 41fcf9de-ab29-3d74-8083-313c71aafb89 | -11.2433 | -50.2859 | 2025-10-07 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 6a493c5d-7721-367a-af4b-52aa27699f64 | -3.4366 | -43.1532 | 2025-10-07 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| ae586f07-99f2-311f-bb25-ed1de78ca2d1 | -14.8645 | -51.4158 | 2025-10-07 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 48ac06d0-8401-3407-8a64-1a3b920b9b9f | -3.4179 | -43.154 | 2025-10-07 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 1936b43b-ba36-3fdd-aeb4-4083c581fcfc | -8.4821 | -46.3136 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 50901572-d94f-38e4-849e-cc7a0f53bc79 | -11.6647 | -44.2702 | 2025-10-07 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 202.4 |
| a5189fbc-ac6d-3b90-828d-64faf7af21b3 | -13.5855 | -51.7994 | 2025-10-07 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| e6d7c0e9-8109-3191-8fc7-41cc223464e0 | -13.8667 | -42.3164 | 2025-10-07 14:30:00 | GOES-19 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 26ab6578-0127-3546-97b8-f46dd0c9b9be | -9.6614 | -45.6667 | 2025-10-07 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 14c31a0f-68c0-39d1-95ca-565cf7c64fda | -8.4819 | -46.3361 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| bf039a87-2d95-3e82-90e2-639117d6c93e | -4.4446 | -43.2164 | 2025-10-07 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 137c85ae-7eb4-34f2-9be8-1aff299926ae | -10.8921 | -51.0269 | 2025-10-07 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3e4a9e38-0bbf-31b5-a0f7-d3b1ff09e23d | -9.9398 | -50.2091 | 2025-10-07 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4d8254de-a0a2-3e05-b8f2-b8f60f4848bf | -12.9297 | -54.7127 | 2025-10-07 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 3066d20a-e7c4-326d-96c4-1a2d65ad64ed | -1.3932 | -49.0387 | 2025-10-07 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c979d8ac-698e-35b9-bafc-86b03a63d1ac | -9.2976 | -45.98 | 2025-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7a128a1e-555c-391c-8c02-30505a629f18 | -16.0012 | -50.9674 | 2025-10-07 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9c787c4e-b3cc-3bdd-b8bf-2e10d4e7c261 | -10.3854 | -47.9956 | 2025-10-07 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5be35a0d-cf03-3861-b9f3-3413637c05ea | -13.7927 | -45.7627 | 2025-10-07 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| eb8150df-4ba7-3b19-9ff9-d7df1ec485d1 | -15.6075 | -42.3707 | 2025-10-07 14:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 08d87cb2-7470-3542-bef7-308eeb29f8bb | -7.8823 | -47.8088 | 2025-10-07 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 752ae0f7-e98d-3c30-a945-6f216f4b20cd | -9.8333 | -56.3748 | 2025-10-07 14:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 11636d18-8a91-3000-af9f-dc7a49c6bbe0 | -14.9414 | -51.448 | 2025-10-07 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ba82ca6e-5235-37a9-8cbb-498fa938ce59 | -8.8618 | -46.0949 | 2025-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 97e7aed3-96fe-3fa8-b22e-c68d374bd88b | -9.9207 | -50.2323 | 2025-10-07 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 9c51a1f7-5011-33e5-9644-6cfcd563f043 | -11.2436 | -50.2645 | 2025-10-07 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 1c4a07c5-9cb6-3a98-89ff-f2cb214cfc7a | -7.6651 | -45.4245 | 2025-10-07 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3ca1a862-8ffb-3101-bc83-46b374eb3168 | -15.6007 | -52.5529 | 2025-10-07 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a52db83f-450c-39a8-afca-7b23b75b0bbb | -10.8919 | -47.1153 | 2025-10-07 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 258.8 |
| a2561232-c381-3901-84c6-cd352d524622 | -7.4669 | -43.0674 | 2025-10-07 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 50a29053-dae9-3e75-9689-d818ae537a90 | -8.8615 | -46.1175 | 2025-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 1b4eb352-8557-320e-b5df-f879b3bf8e86 | -7.7182 | -42.5688 | 2025-10-07 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| df2eb8ae-cff4-3a05-b799-4868f31ba011 | -10.2129 | -54.1262 | 2025-10-07 14:30:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4c97e987-0b07-3b24-adaf-1b81c2c4c173 | -10.2057 | -46.0319 | 2025-10-07 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 2e122e7a-8eb3-3487-9d47-a1a917497b72 | -12.0318 | -45.1669 | 2025-10-07 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 1b9046f5-16fc-3864-94ad-3e0e20218c99 | -11.8635 | -44.938 | 2025-10-07 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 6cc2ea6d-a914-3cfb-9a18-1570cae36493 | -6.0804 | -42.5354 | 2025-10-07 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| c8f0cfc5-1b89-3102-8d4e-cf5bd92879a1 | -10.3057 | -46.9635 | 2025-10-07 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 1253bcd5-4b15-30af-825f-c5bdf43811fa | -9.7463 | -47.7144 | 2025-10-07 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 87a77c11-c66e-38a4-8b28-b209af9ffccd | -3.1953 | -42.907 | 2025-10-07 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| aad05ba7-85fb-349f-875f-8823d808428b | -14.8884 | -47.2226 | 2025-10-07 14:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 47306801-ba7c-3c5a-ae59-1d47461ce9bb | -14.8637 | -51.4589 | 2025-10-07 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 03c13442-8bd0-3d00-9019-5b1e2a55e3c5 | -8.4824 | -46.2912 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 0e51bfc3-7e2f-3a9c-84c4-85a50152430b | -15.5877 | -42.3751 | 2025-10-07 14:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9aa1f18e-6830-3889-aaed-b4e23437c9a5 | -3.2713 | -42.6457 | 2025-10-07 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9eea3d8a-4f1d-3f71-b2ad-a2efcf3d762d | -11.1644 | -54.8804 | 2025-10-07 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 179.3 |
| bdfa3845-283e-3633-8094-f518a417d41f | -7.2416 | -42.9957 | 2025-10-07 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| ee81c6a0-a1e1-3d42-aff8-62d58a3a5325 | -3.3093 | -42.5263 | 2025-10-07 14:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 12cfb222-4a53-3225-b70f-5d54d5b1a5aa | -3.8759 | -41.5708 | 2025-10-07 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| ad735999-57f4-3dfd-8a4d-e6808f5a1442 | -8.5007 | -46.3342 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 00474a94-b977-3f72-8e86-0cff5cc7a97c | -4.0569 | -42.5118 | 2025-10-07 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 158.9 |
| dedfca70-be13-3323-a840-a92db552715e | -8.8429 | -46.0969 | 2025-10-07 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5ba7aae7-0c34-33ad-9351-8915c06a384a | -8.6208 | -47.2788 | 2025-10-07 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a65c8e0c-1e58-3e55-946e-b93b5c72fe78 | -4.0382 | -42.5129 | 2025-10-07 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 4ba8ee2d-731d-39e5-9826-fc6e19957222 | -15.6198 | -52.5715 | 2025-10-07 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9a549e7b-f759-3dda-83ce-68607d86a8aa | -11.6839 | -44.2673 | 2025-10-07 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 198.7 |
| ad42a37e-bf1b-317f-ba1c-c016fff4c4fe | -11.0073 | -52.3196 | 2025-10-07 14:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a989ad64-2635-3103-83ac-6f2f09ccb3b5 | -15.6003 | -52.5742 | 2025-10-07 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 4c53fe4b-7418-385b-a3f4-0b73b7b4b6cd | -1.4116 | -49.0597 | 2025-10-07 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b9af7599-eb4d-3a36-b324-50bd0c18bd8a | -11.8029 | -45.1087 | 2025-10-07 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 74b2c037-70bf-33ec-a447-a0b5f5bae0e2 | -11.8038 | -45.0624 | 2025-10-07 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ffa11e5b-73f7-3925-8a89-749dca2f95d4 | -9.3382 | -45.772 | 2025-10-07 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b1111e4a-5b9d-3337-b55a-d678d2781446 | -15.5808 | -52.5769 | 2025-10-07 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 690e29ff-b8a1-39e2-a20b-babed74bfeba | -11.7837 | -45.1115 | 2025-10-07 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| e13ab443-9268-31b0-b6b7-32a147772354 | -15.6202 | -52.5501 | 2025-10-07 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 692fda6e-4f41-33e4-b4e6-5d85314b8fdb | -11.8823 | -44.9583 | 2025-10-07 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 197a7321-08ba-33aa-8bcb-7b0c6bfb9fff | -10.0868 | -50.5141 | 2025-10-07 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| eb0f0bda-e20a-3617-bfe3-1f09a3dc2b12 | -8.8717 | -46.7878 | 2025-10-07 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b18bbb56-43c1-35db-bcf3-6f6dd6ac397f | -10.9113 | -47.0906 | 2025-10-07 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 222.5 |
| c6f9bdd8-f84a-37df-a418-8667e3cab51e | -10.0506 | -50.39 | 2025-10-07 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 104d3657-c96e-3cea-88b0-d799e54ef946 | -11.0448 | -50.926 | 2025-10-07 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 236f7d7a-8c01-3b2b-96b1-53a902ee8cf5 | -10.325 | -46.9388 | 2025-10-07 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 4e35e6a4-87a2-3c5b-9ee7-2838dea065d7 | -13.3291 | -47.7641 | 2025-10-07 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| f4731020-8023-3329-8cb2-7bfda37dc99b | -14.8447 | -51.4401 | 2025-10-07 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 602a7185-560e-32a0-b2c1-b3c69b4f4051 | -9.6804 | -45.6645 | 2025-10-07 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 341.7 |
| b508a4ce-b557-3dea-97a4-eea29c3c79b0 | -3.4356 | -43.3394 | 2025-10-07 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2fecae42-b2c1-3a97-b1a2-eb6aa44d5bf5 | -8.1702 | -44.1377 | 2025-10-07 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 0adfae53-5497-30d9-9c13-badbc67af03e | -11.8038 | -45.0624 | 2025-10-07 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| d03ddf8c-2549-30fa-92ea-8f48d19bcdc4 | -8.5599 | -44.6494 | 2025-10-07 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 02301962-ebae-347b-aa63-9aac7daa6447 | -3.3986 | -43.2714 | 2025-10-07 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 31b9d901-d247-3d6a-828c-b282cf50329d | -3.3093 | -42.5263 | 2025-10-07 14:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f5ccf065-9be9-3e03-a47d-821b3c207d92 | -4.0569 | -42.5118 | 2025-10-07 14:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 142.5 |
| aaafb2d0-50de-39e2-a964-4cd7c2f98efe | -12.0318 | -45.1669 | 2025-10-07 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 58bca403-e373-3307-98e6-5151f4ab25e0 | -8.6519 | -46.2964 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ea5ecc29-015e-340a-9e29-a650149cf532 | -3.2712 | -42.6692 | 2025-10-07 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 518d974b-09d0-30cd-8e2d-3e6422b43364 | -3.2696 | -42.974 | 2025-10-07 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 82fdd2bc-459a-3340-b1ab-44c3e14f57d8 | -8.9759 | -47.4864 | 2025-10-07 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| bbcb1bf1-3481-3954-83c8-0a612d6884bf | -8.1888 | -44.1588 | 2025-10-07 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| c1bda4ac-0b4f-3ee3-a2d7-25c5b638f64a | -9.486 | -46.0265 | 2025-10-07 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 1e079197-cbbc-3c92-8d26-e16a5db6fe1e | -3.4542 | -43.3386 | 2025-10-07 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 3dac9640-2aae-3221-837f-c13b5912adef | -10.0217 | -48.2994 | 2025-10-07 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 07b44710-1853-3731-b3dc-3d17e4b6b795 | -10.3348 | -50.2974 | 2025-10-07 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| f1f568aa-cb76-3e56-ab1c-05425d6a469a | -9.4178 | -46.8637 | 2025-10-07 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7ebc7344-f62b-371a-904d-219548c7e9d0 | -10.8731 | -51.0289 | 2025-10-07 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d6d4f691-d328-37eb-9020-1386002eec39 | -8.8618 | -46.0949 | 2025-10-07 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 7f8656be-69cb-3ed5-9ff9-feeebf122d12 | -11.0073 | -52.3196 | 2025-10-07 14:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |


[Clique aqui para ver as próximas entradas](README130.md)
