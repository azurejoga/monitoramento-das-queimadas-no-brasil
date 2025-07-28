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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fc48dd5-5184-3b42-abe7-0ac26cfea47c | -6.49428 | -56.20253 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7d15a6-e507-3534-9bb8-b7f20c15a0e7 | -6.39841 | -53.32887 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffa5f061-7c64-37dd-b4e3-a8be1651c417 | -6.40242 | -53.34923 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d00ce61-7a56-3435-ad05-7afee7aff04d | -7.24167 | -45.38837 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64f45f73-efb0-369b-8022-2cfe56706b53 | -6.54319 | -56.18927 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a96cb406-b3ac-325e-a122-e6b282370e95 | -7.24645 | -45.3976 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51743598-2a21-3d23-ac14-4a14368b90c9 | -6.89079 | -52.8662 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99bffaee-5047-3d13-aeb3-afb01b1cce80 | -6.49539 | -56.19557 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ecb07be-2547-3a84-b3eb-5a909073fe0f | -7.54213 | -44.43037 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d93e7d0-9b21-3f43-8217-9b710aee0ef8 | -7.75086 | -51.11221 | 2025-07-28 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be89b59-660e-336d-ab8e-14308d4a49ea | -6.40182 | -53.35309 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2e74012-53ad-3b35-b403-fb943a80f091 | -9.29303 | -48.32657 | 2025-07-28 05:06:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 760a9d28-157e-3bf4-b1e4-1bcbbb04e0f7 | -9.29375 | -48.32752 | 2025-07-28 05:06:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d065db00-9c2a-3792-9e15-8ff696c28ef4 | -7.11641 | -44.91475 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 17ba1ebb-4b7b-3b9d-ac02-fd775f01f6eb | -8.30838 | -55.10068 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e78e14e-a697-3d7c-aa22-2dbdbc62babf | -6.39714 | -53.36027 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa3d93d3-69f4-3fd2-ab55-3fe2d775a0b0 | -6.25584 | -44.96754 | 2025-07-28 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9f56ee1-5ca4-3853-8993-3e4bdeca8b2d | -7.21329 | -44.16407 | 2025-07-28 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98a8f0c4-5157-35c8-9863-5574e9aba96c | -7.24699 | -45.39346 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bac5893e-769f-33ec-998c-31ecd31867ab | -6.54873 | -56.19727 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99c7d5cb-093a-370b-8fd5-4ef617208eff | -10.52007 | -42.55827 | 2025-07-28 05:06:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3294cf9-e9e8-3082-9fae-ab42e088df1f | -6.49483 | -56.19905 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c6b214c-01de-39e0-9f79-2102628a8bc2 | -6.54928 | -56.1938 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5475ed66-78b1-352d-9b46-b7c84e2d2051 | -7.69223 | -46.04631 | 2025-07-28 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 110b8d61-1b47-3f6a-b7fa-a288080c4dd6 | -7.74684 | -51.11167 | 2025-07-28 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 527254e9-beb9-3261-8b9b-071803445145 | -6.43958 | -53.34686 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae84ac4d-cdd6-313d-9460-b417f2b2b16d | -6.88331 | -44.79515 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b22c67dc-790c-3bad-b39e-6928b2b7fbd2 | -7.24112 | -45.39258 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7e45db6-e976-3112-bced-4ffc98d99ea1 | -7.81187 | -44.59319 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac590b5-3c13-30cf-a82b-69a159583f09 | -7.24057 | -45.39679 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7059cda9-8d4c-3b2e-b1d5-b3092c873c49 | -6.54264 | -56.19274 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05288394-2fc5-316a-b689-77ad8409ad2d | -4.30841 | -48.09774 | 2025-07-28 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a3ee2fa6-f8ec-35df-8440-cdcabb49d536 | -6.49595 | -56.21349 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e3f0ca68-399a-3a7c-ad74-7850ab4c2c48 | -6.40472 | -53.3575 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 233d01ca-b8d7-35e5-b180-cd0648d39604 | -6.25934 | -44.96859 | 2025-07-28 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f68990ea-157a-3e56-aeb3-c41d65782857 | -6.50093 | -56.20359 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 154c7156-f922-34b6-9d0d-6aaa711c5049 | -6.45121 | -53.36446 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab5042e5-cfd0-3ed7-a5a3-ab665f163416 | -7.80697 | -50.77865 | 2025-07-28 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 30e01f4a-f229-3de7-ac77-12e8d49dfd0e | -7.29859 | -43.07973 | 2025-07-28 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 53ad8b8b-ff5e-35e1-913b-e4d2faebc279 | -7.11 | -44.91214 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 49ad99d6-af9d-3e54-896c-a0131259ca74 | -6.88271 | -44.79953 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a449fc5-922e-38ca-a064-d2b4c21a10e8 | -7.09365 | -44.94747 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b102043d-a0e2-34f5-bb27-77a9904ce29a | -7.10049 | -44.93633 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef4ddcec-e1fb-3085-952b-38540cc3e5e7 | -7.65489 | -44.79774 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e3e2957-c253-3d51-bba1-c3b2897c20a9 | -7.11036 | -44.91393 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a12ccbc3-e74c-3f57-aba2-e010363225d4 | -4.30771 | -48.10264 | 2025-07-28 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d3cd749-4f92-3252-ae7a-d4ee5c1894a1 | -7.21261 | -44.16903 | 2025-07-28 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27a2c3b3-8959-3772-88fd-0d51eee37277 | -7.65545 | -44.79335 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce0fae94-c613-3c32-b7fc-26a547002805 | -7.0773 | -44.92593 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d3b49eb-d871-3134-aa7a-6f749d645c04 | -6.49373 | -56.20601 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 312f962c-3979-3df3-8f75-1c361e3ee28b | -6.4094 | -53.35033 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c1b33c-987d-373a-bbc3-35f58e62b661 | -6.89017 | -52.87029 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df2c718d-8792-33fc-9cac-862f31b4848c | -10.45999 | -46.51345 | 2025-07-28 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f114d88c-7efe-3daa-9312-c3862647ce4f | -7.74231 | -51.11465 | 2025-07-28 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf3086ca-5475-395d-9643-e8ad87836bf6 | -6.26239 | -44.96403 | 2025-07-28 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba281685-43c7-3ab6-a8cf-f7ed56991ad6 | -7.69549 | -46.04429 | 2025-07-28 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2989ff2-0e34-3340-9f23-79d33d6d8533 | -7.0955 | -44.93336 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe23742b-7264-3cbd-8bb7-4224ca541fcf | -7.07979 | -44.90781 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7be83049-dc1f-31f5-bcb8-d385982b7f57 | -7.084 | -44.92197 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e0a0b42c-6e11-35af-8748-63bec64ec865 | -6.54651 | -56.18979 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 206a8074-f874-36b2-bbc2-18afc9d315fc | -7.5328 | -44.40425 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82b900c4-4251-3cef-a401-eebf3b78b44c | -7.0924 | -44.95033 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10dc93a1-d065-3432-b518-a91ef3a62965 | -6.49096 | -56.20201 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2c010b6-feb3-3cbb-90c4-2bfc4b071bfa | -7.11605 | -44.91294 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a237240-b3c9-31c4-868f-03d28fcf1926 | -6.5037 | -56.20759 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0aa717b4-7c9e-36e0-b123-bce9a1956767 | -7.66036 | -44.80373 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3844fa31-92de-3147-a449-fc8a298c1e14 | -10.52094 | -42.55071 | 2025-07-28 05:06:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 89010465-259b-387f-b316-d938d92fe14a | -7.6979 | -46.04708 | 2025-07-28 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3b8e169-73b2-3e7a-8055-fb6c838549e8 | -7.07314 | -44.91135 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e4043a5-42f8-3e3c-ab51-9b2f79e56959 | -7.65543 | -44.7941 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79e6c3d8-24a7-342e-b4ce-c039995d9a5c | -7.69443 | -46.05198 | 2025-07-28 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5105dfa2-76bb-3b32-a614-989348894ef2 | -6.49041 | -56.20549 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 486d59c5-6177-3ed5-a402-fe02c7b5b5dc | -6.4483 | -53.36007 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f48e0a8b-10e6-3ae6-b546-0676366920d7 | -6.49761 | -56.20306 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66d3bc94-761d-3ac0-993f-da36cf032a5e | -6.54209 | -56.19622 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6f344e0-c709-3e42-ab3d-f9f16cdb495d | -6.25776 | -42.83939 | 2025-07-28 05:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 432560cb-519c-3e99-9c7b-6bbd77f2723f | -7.74183 | -51.11802 | 2025-07-28 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d29826d4-5a68-367f-93b1-56f9e4949ac4 | -7.15384 | -44.36435 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 399b40f3-4df8-306c-960a-fa32859b10a3 | -4.30627 | -48.10077 | 2025-07-28 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 00f848dd-32b3-31e8-8728-15f474cc174b | -7.08041 | -44.90321 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f25e292-3370-3939-b451-9ef9299ba8e0 | -7.69496 | -46.04813 | 2025-07-28 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3375f6-ebb8-3d17-9eb4-dd4288ac633c | -7.093 | -44.95242 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74216627-de68-3bbc-beb9-3af2f9d1bf11 | -6.50148 | -56.20011 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 412c8130-473f-3eb6-8de2-4381a4cdbe87 | -7.10984 | -44.91788 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f1762187-dad6-3618-820b-fcc9dd0c4bdc | -6.40531 | -53.35364 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 935af9c1-6d96-3d0c-8e73-c07db3d8dc13 | -6.40591 | -53.34977 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4eaf397-ca53-3506-ab73-5b0618ac5db4 | -4.86601 | -47.75113 | 2025-07-28 05:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a988a019-c8e2-31fd-8f7b-06232aa4c0fb | -6.92534 | -44.2538 | 2025-07-28 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84da12e8-6e0b-3bf5-89b3-756379ea013d | -6.26179 | -44.96843 | 2025-07-28 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 001bc4c1-0f07-3cdb-a6b7-199dca5a6730 | -6.49983 | -56.21054 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2ee5250-5da2-33f8-a9f8-749a0d40b4c3 | -7.29177 | -43.07905 | 2025-07-28 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5af75372-1c83-3dfe-8196-babfa2705b36 | -7.81803 | -44.59454 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f4ae0ae-04d0-3bff-bcb6-28a4164fd4b0 | -6.50315 | -56.21107 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b335a9d2-b3eb-3f71-a521-7ad18ca3cc1f | -7.8075 | -50.77494 | 2025-07-28 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd379a75-7c87-31fb-9ca7-f4b022287813 | -6.53932 | -56.19221 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe73ed37-7e5b-30d9-b056-4ef9be019641 | -4.30373 | -48.09705 | 2025-07-28 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0b39d95e-a453-3b88-965d-6328add0011e | -6.54596 | -56.19327 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c0f4083-0250-3ffb-8b8e-e336fdffb1b2 | -15.36956 | -52.18103 | 2025-07-28 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8765a1a6-61b5-3702-87b5-3b77eafba98d | -9.02229 | -59.76189 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ec3f4c0-d920-3690-87dc-a6b5cb4dcc61 | -14.98371 | -46.97283 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
