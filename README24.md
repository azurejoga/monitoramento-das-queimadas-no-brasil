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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bbd19b5-ba73-35c4-9f8c-12c00b8e60a7 | -7.01067 | -45.25025 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ee655c57-8908-3b38-80aa-24c2d8530994 | -5.66534 | -43.40549 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aaa2fdb-519e-35f7-be9c-ff53aa09643d | -7.74127 | -46.71517 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97e9857b-3d50-30ea-abac-beb6009822a0 | -7.626 | -45.45543 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38a31c6b-69e4-353c-bd79-19fc253864ab | -9.28779 | -48.19613 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f921062-c538-35e5-aeb1-615551fc5034 | -9.26207 | -48.2057 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b55b7d20-6780-31c2-816b-27313d3b1be7 | -11.23779 | -48.38056 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 735e8f19-5b4c-3a3f-a976-e0e42df3ea14 | -9.05058 | -48.72396 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fcc0e3af-e1cf-3840-80c1-96b3813e1c30 | -12.01446 | -44.68573 | 2026-09-20 04:19:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81a2dd3e-f42c-3ed7-96a2-4a04cb20c35f | -7.69664 | -46.1088 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2d46b37-53b3-3fbb-bcf6-e75eff5ecc46 | -6.29764 | -47.62494 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e8942ac-bc88-3c13-92d3-b5ff36625578 | -9.17048 | -51.50916 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d500cee2-8d82-37c0-98f6-1d5aef391088 | -11.66451 | -43.42501 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1abfdb2f-8a73-3582-aa79-0c1919335b81 | -11.00713 | -48.31398 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb43b56c-c7de-3900-898b-be761180d8e7 | -5.57342 | -45.5505 | 2026-09-20 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 167a02bb-a337-36cc-8fa4-236577651747 | -7.02766 | -42.08173 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b304f13d-f9d9-3f15-9d68-31366c8e05e9 | -8.30315 | -46.85842 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3f420df-9bc6-330e-a606-080ba9fc2d5a | 1.01825 | -51.18439 | 2026-09-20 04:19:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a140f2-843f-361c-93f9-ea9755435dcf | -9.77091 | -45.06538 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 048e7c39-cab8-32c6-a8fe-510b3d6a1733 | -11.4522 | -45.37622 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59118dcb-efed-3013-8150-03701b719d87 | -11.4588 | -45.40213 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aac8b30-d90d-37de-a6ea-910e4d826867 | -9.8335 | -46.43892 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7fd58cd7-ef31-30f6-a851-5cdb91ebe14e | -9.02629 | -48.75708 | 2026-09-20 04:19:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f7a77f0-c74d-356e-a2ee-c3ab5a5f2b6e | -10.30672 | -50.24018 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffc9f992-f91a-3f21-88f0-1d91989ce405 | -11.34566 | -43.38689 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae1f44ce-baf2-327e-8e04-9387ef1da42c | -9.75782 | -46.06788 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 760925a9-c1e7-3898-a01b-90701e584d6f | -8.93673 | -44.38891 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38bfd469-c90d-38b0-96d7-422920e6f538 | -3.44577 | -50.60604 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88b27035-2b75-34e8-a1e3-bb4bc4bd9297 | -3.00242 | -54.16613 | 2026-09-20 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cd269d4-2114-32b7-b8c0-445fa9b113e7 | -10.48876 | -46.27345 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2c0b60e9-7afb-3e70-8d30-23ba8a9af51b | -7.49228 | -46.71278 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2ab2c0e-4038-333b-afe4-256c7bb33e58 | -5.85751 | -53.54125 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7770d5ff-d4d3-34ee-86ca-b0676f5bc507 | -3.73753 | -51.81994 | 2026-09-20 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c87a39ee-4811-3e10-8019-c31958409198 | -6.39896 | -43.19326 | 2026-09-20 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2852f2d2-9ae5-3eaf-a3dd-9b35b649b078 | -11.32388 | -47.28038 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50eec75f-5e10-3780-81bb-62d5ba69f474 | -6.29578 | -41.76842 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d9ffb9d2-ac55-38fb-ad2b-bfb1d2e42064 | -7.63687 | -45.82436 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 607d6d43-9a12-37b2-9213-faec4cbba502 | -7.53722 | -45.42886 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 64b68824-af30-302c-a332-a38e798fdeb1 | -10.47588 | -51.26622 | 2026-09-20 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65f50ced-5a9f-3301-b145-294cf7293569 | -10.3246 | -45.33239 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01c9b672-37a5-3cd2-b67d-b9da744fe53e | -8.49986 | -47.43401 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2c31f6a-a319-357c-9a00-e74a111d0a61 | -5.6625 | -43.40116 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f67e5c50-2366-30ca-a854-b5bda057f390 | -9.80087 | -48.31673 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 168bcc5f-b695-3e1f-a9f7-9107726255d7 | -9.24299 | -46.18307 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4346191-75d9-3086-9f08-352c32b116e5 | -6.75707 | -47.88373 | 2026-09-20 04:19:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8aec74b-6406-3dfc-9308-2d324600f9d9 | -11.01776 | -48.32745 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7568f843-4f80-3925-b631-3939ae97ce3b | -10.32221 | -50.20977 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 386f72b8-5ebf-3bfa-93f4-d13ba5717c8c | -10.30581 | -50.2578 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cc1ab55-13e2-3d0f-83e3-e79682c32868 | -7.58021 | -44.9019 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 828d7848-d1e3-36f1-a20a-c86bedc7fd43 | -10.78071 | -46.32961 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18c99af4-c0bd-35ee-b4e9-91072fa34c1f | -8.9972 | -45.00478 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e601726a-8226-3339-80c2-44edd01405ff | -5.84997 | -53.54313 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a898d15d-04fd-3f56-af1e-8c858809923d | -9.80789 | -45.84349 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83badbc6-aa21-3e5d-ba0f-399ee002abac | -6.75915 | -47.92387 | 2026-09-20 04:19:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e40dfd3-948f-3d41-9334-fca9e7261598 | -9.23848 | -45.91527 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b5c17f8-f9e8-3036-8aee-1c2d898fd606 | -10.26472 | -45.4852 | 2026-09-20 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e7b9543-0df5-3b4f-9dda-dcb0982607a2 | -7.59835 | -55.71229 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2bcbf82f-c2ff-3f6c-9b92-dbd124629a78 | -5.32925 | -50.09164 | 2026-09-20 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d22a4f2c-8293-373d-9281-1cb73b1a5ba2 | -10.56147 | -46.5681 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eb1cf82-5c87-369d-a807-1433b59cd8e4 | -3.84481 | -51.33871 | 2026-09-20 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40823b0a-974a-3105-95d9-2f0197d3ffae | -7.01141 | -45.24583 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 10134512-d8b3-3196-ad59-05a8ef1f3988 | -10.30186 | -50.26718 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 98241191-6c5e-37a2-aa50-729c620a6a61 | -5.88734 | -46.5865 | 2026-09-20 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab50b296-c5ff-3e38-b7d1-a27811a59a20 | -3.95829 | -49.04426 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c068472-8128-3feb-9b5e-3d90be08286f | -8.18539 | -54.75714 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a425f4a-996f-3e1c-a685-05bfe2c5daac | -6.02557 | -45.40937 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bb09c62-64f5-35b3-ab45-067eb90b7522 | -8.06235 | -46.83265 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 376865ca-437e-3fb3-815a-4153e3554064 | -10.29321 | -50.20422 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee037041-f973-32bc-bd3a-54e2d0d9b568 | -8.43708 | -46.85885 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c779af36-3f18-3087-8ca5-d81a63dc115d | -7.35989 | -44.878 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b08fdcd6-f205-331f-92c7-5510a458e2c5 | -9.83267 | -46.44374 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7580feb8-4481-3e7a-a5f4-82914a565337 | -6.17486 | -47.71386 | 2026-09-20 04:19:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 899a1505-03a6-3eaf-96bd-fc1ef859351b | -11.15021 | -42.79315 | 2026-09-20 04:19:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15a1ec3e-822f-3e58-b677-fbdd3a136ee6 | -7.15843 | -47.46488 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2163c91-c46f-342c-b763-b0ee5dca1a6b | -10.23812 | -45.35706 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71ce0b89-69cc-33a3-b9bb-c6f57ed80eb1 | -7.16059 | -47.47759 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 377e02be-362c-3dee-9c70-96c5cc60a0ec | -11.50118 | -47.78839 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d993989a-8c7a-3fcd-a8e3-5120f40b4cbe | -10.7804 | -50.87901 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0bc9cc38-fe98-373a-83ee-fa7e2088da2b | -11.44479 | -45.33366 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebe1536b-3a43-38d7-8b13-b5ba4a00ff21 | -10.3159 | -50.20411 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a672bfc6-791d-318d-9180-9c2d40db878d | -5.76241 | -47.28778 | 2026-09-20 04:19:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7700d0f2-37aa-3831-9f8f-c7e56bb0d41b | -6.98633 | -45.8049 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5043198-e368-3aef-99d8-04297416cc07 | -10.78147 | -46.32509 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cacd171c-fe64-3f01-b211-70a11ddc781f | -10.31834 | -50.20346 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 804153f8-dec8-33e8-9e8a-659c336922ea | -7.96168 | -44.06368 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b72768a-8ae5-37e3-bba3-0d01dfb38e36 | -7.27786 | -45.54663 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c663f29e-0415-3140-a1c6-d2e04d39f60c | -6.93042 | -43.10575 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac146d37-de3a-3470-b7e4-e5afc547c00e | -9.72638 | -46.09286 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d250137-c84b-35b5-85e3-8edf8e14c408 | -8.44933 | -44.69912 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f7b3ad9-aeca-3d38-8efb-0a38ed328b25 | -7.44996 | -44.73849 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8bdecc7-20aa-35ad-862a-d5afa44e88e5 | -6.7234 | -46.07713 | 2026-09-20 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3864d76e-6e30-3284-9d85-44ebb145443b | -7.00963 | -45.76038 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e0983fd-1a38-3f91-a813-754c7310d184 | -8.17551 | -54.73686 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39f4a0fe-e4e2-3451-8634-b2fccdca8772 | -8.17874 | -54.75568 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a719af80-1366-3436-a8d6-e473365d52be | -5.63554 | -43.38154 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c98a8fc0-ecd3-3860-ae2e-7d02a619089a | -6.29541 | -47.61176 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a4d65de-c857-3a4b-9df0-a2a292b3dae1 | -3.4408 | -50.60143 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90c3360a-db32-36f8-8680-47bada99c67c | -9.85946 | -48.34443 | 2026-09-20 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11f43e99-4668-3829-95f3-09592a335de5 | -7.3718 | -44.71382 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23c40b34-ba1c-33ee-adad-33273409962a | -11.04354 | -48.30476 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
