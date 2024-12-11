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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2a411f4-3165-3ace-a941-9a6726a6a1e9 | -11.14771 | -54.23114 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe9ad8d5-a021-36ee-b8a0-f11bbf0735cb | -6.96417 | -43.00251 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 45b12bca-3726-31c8-8ef8-8faecd24a361 | -6.94696 | -42.99852 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c02c51b3-94f3-3956-b08a-ca974f585e76 | -12.4132 | -43.80163 | 2024-12-11 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a22bc133-59f5-3493-8a2f-d86fbd7fe261 | -9.71684 | -54.89294 | 2024-12-11 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a200589-e81e-3b96-93fd-299e3bfe4c79 | -6.97225 | -42.98927 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 06eb5622-f1ea-33f9-bc17-9dcb45f7f0f5 | -6.95925 | -42.99196 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 8f998917-7b0a-33c2-a4d2-de9d86d14997 | -6.90291 | -43.50903 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 535afa3d-77be-37d7-8339-ecbace102601 | -6.97779 | -42.99505 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c0c76127-094d-32bf-88e4-e662dba65b40 | -6.89692 | -43.50813 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b432ca88-ed26-3fa0-9817-999c542e060f | -6.11848 | -42.54602 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d7b169ab-f4cc-3f8a-ab00-fa55e734d819 | -10.76885 | -58.83966 | 2024-12-11 04:57:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bcee827-3041-3a7d-903f-61d59c8c5f0c | -3.81149 | -54.60497 | 2024-12-11 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6ef4e06-a840-3545-b649-4f1c93cc68e4 | -6.95249 | -43.00416 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9099ece1-4645-3528-adb9-b2897d42b9f8 | -6.12756 | -42.52685 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a14195e-e9a0-3999-a6f1-9eb667a2fc17 | -11.11236 | -54.63885 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f060f83-750c-3244-b7bb-725e7da8eec4 | -6.95381 | -42.99467 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 76e56592-66f2-3aef-870e-87800e3ffe7a | -11.09787 | -54.62199 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54d43d26-b90d-3f3b-ba12-899a1e101512 | -6.65776 | -54.93911 | 2024-12-11 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27c6970e-5da9-32f6-bc37-500e3a8b56be | -11.10065 | -54.62608 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc97dac6-f7d7-34c2-a360-59edf77e496a | -11.11181 | -54.64239 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5960699-5ea2-32d8-a3bc-e5d4bad1b129 | -11.11625 | -54.63583 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c1f6d60-c86c-3aae-9699-bd19d699df16 | -11.09841 | -54.61844 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fec02492-2c85-3f9e-84fc-179393dcf92e | -6.12616 | -42.53694 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d5d9ee96-3179-3f09-8188-0ee57c7b7750 | -10.02798 | -53.7519 | 2024-12-11 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69aa9822-0571-37d1-acbf-467f9dc11a41 | -6.95988 | -42.98719 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 85e9882e-1613-3b1e-8f91-464e09acd7e1 | -6.95933 | -43.00034 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 29cebf90-1ddd-32d5-a1b7-36735c207e8b | -6.96544 | -42.99296 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4a2c5fa8-2c53-3368-9571-2a770313e789 | -6.8975 | -43.50377 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 33ffae7c-737b-3262-b331-42d912d08d9d | -6.9359 | -43.53599 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb677104-ff4c-3ee2-8dd2-8a6dff954da1 | -12.67129 | -45.67485 | 2024-12-11 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7d831641-6c83-369c-a78f-8e76e59d570e | -11.87037 | -43.7177 | 2024-12-11 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8f1360b-98ee-362d-8b6c-6c5460a780ae | -11.10902 | -54.63832 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe5a2d24-ca8f-380d-8b60-bc77876b6364 | -6.94761 | -42.99377 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5d5fca03-ff2e-3390-83b8-76378f75a541 | -10.96248 | -54.09573 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b26cc7a4-9c67-3b4c-9461-6b487fdfa262 | -12.05523 | -46.88925 | 2024-12-11 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 212f3911-7ed3-3a80-b165-4f538f93640c | -6.12476 | -42.54707 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 84c00e89-fdd6-327c-8e4c-2ae4f94090b1 | -6.12546 | -42.54205 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f25e6910-77b5-3610-8567-42cc9bb1eba5 | -12.05659 | -46.88948 | 2024-12-11 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e5df253-be78-3ca8-8d30-a9e412c002b0 | -6.95799 | -43.00152 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| c886aefb-8a6e-3b41-9652-ffaff6e483ac | -9.72072 | -54.88998 | 2024-12-11 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b33349c-e741-3c5c-b2e1-2dbb1453e561 | -6.9167 | -43.49737 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cca3dd0-f29a-36db-9bcb-12002a1688f3 | -6.96606 | -42.98824 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 85bdb660-e68b-3af3-b331-4c4380f5a752 | -6.66165 | -54.93615 | 2024-12-11 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aea6dc5-e348-3906-95f4-3791ec814fa3 | -6.95243 | -42.99582 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f6946f24-b977-33eb-81e4-6b5f11a38eb2 | -9.71739 | -54.88944 | 2024-12-11 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4bdede-5122-38aa-b9d4-ade2b0868224 | -9.26108 | -63.26311 | 2024-12-11 04:57:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 171dcdb2-2398-34e0-9135-ccbd2516514f | -6.89573 | -43.51698 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 29a7a06e-a25d-358d-bb1e-a7eefbc5cf91 | -6.97035 | -43.00352 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 13268048-346a-3ed5-a5a3-9d26f276e2c9 | -6.11916 | -42.54105 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d680fbf1-d5a8-3915-b2c4-da633f44d67a | -12.85306 | -43.81884 | 2024-12-11 04:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 555f5fb2-09dd-3ec6-890f-fbe18571d9a0 | -9.19481 | -49.47407 | 2024-12-11 04:57:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 205578cf-ecb3-35c8-8851-9d39ca800767 | -11.10289 | -54.63371 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68ac3179-982f-3200-9934-cf3df6e2f0d5 | -11.86978 | -43.72274 | 2024-12-11 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f214ec44-906c-30f0-b93e-8d9c7b3c1e61 | -6.12056 | -42.53093 | 2024-12-11 04:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 157a1962-7174-32b4-ae32-04201bc1549d | -11.09453 | -54.62146 | 2024-12-11 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daea8964-cd9d-3acb-ac3c-f5fb95652f83 | -6.90232 | -43.51337 | 2024-12-11 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 288e5e05-9aab-318d-9ab5-5e52df511ece | -6.67109 | -54.91971 | 2024-12-11 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8df492c-8c23-3a7e-92ad-00bb751d81cb | -6.97162 | -42.99401 | 2024-12-11 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c3456cf8-34b6-3d19-bd5b-a2c5c4f1842b | -12.53536 | -58.34144 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb76408d-3ca7-3e95-9379-6c8a9f2fcce5 | -15.07742 | -59.65244 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ab1dbe1-f9d6-30ed-808a-d8eba0248f7f | -15.0208 | -57.61693 | 2024-12-11 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89d5b004-81bf-3189-90ad-774e61fca236 | -12.56228 | -58.3545 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c0126145-ee02-37ac-9ce2-bfbf22892855 | -17.74422 | -54.2181 | 2024-12-11 04:59:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1feb4d-9a30-35e3-8105-869f1f9b4aeb | -12.54666 | -58.33923 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afee06a8-102d-3431-87e9-ddd97de42175 | -12.55304 | -58.34455 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 62b27004-f959-3109-8d02-8b01cb0d718e | -15.08182 | -59.64874 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d50bdfb6-bc00-3958-8644-2aee4935ae02 | -12.55942 | -58.34985 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b583ae31-4a81-3bc4-aab6-7a1c94d62d8e | -14.81965 | -46.95657 | 2024-12-11 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b53e7302-7cb9-3e83-90c8-68003bf727c8 | -17.23982 | -54.45053 | 2024-12-11 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84eb83e9-fd13-34ca-aca8-d3a700737280 | -12.54107 | -58.35073 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 54178eb9-71cc-3c99-90a1-ca1833e97be0 | -14.28339 | -57.46552 | 2024-12-11 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8771784e-f540-3c26-b99b-262b2c7aca8d | -12.54255 | -58.36348 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ae7c2627-6ec4-3076-ae05-8113cc6d32ea | -12.84666 | -59.03367 | 2024-12-11 04:59:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1df0150e-fa61-37d6-8a41-45626a107d09 | -12.54244 | -58.34265 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 69b1a883-3ee8-3984-906f-e592ecc553d6 | -12.53182 | -58.34084 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 253148e6-f1fd-366e-8489-a61e6ecdb570 | -12.53156 | -57.7221 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c246600-9250-3add-99c2-f39e22a352c2 | -12.5638 | -57.76317 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c063977-4624-3932-8185-148e3d83588c | -12.53467 | -58.34549 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d80a0763-b797-31c9-8a2c-b71db0b528f2 | -12.53872 | -57.74305 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99220c40-fb82-30ed-9ffd-b881f491c636 | -12.844 | -59.03076 | 2024-12-11 04:59:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8591c253-29eb-32fe-9447-bfe9fe3353c7 | -12.56093 | -58.36254 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5f6d783-09a4-35c1-b375-2a93a7d0d292 | -14.97384 | -44.40805 | 2024-12-11 04:59:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24e2f5cc-327e-3082-91ba-b0ea3d7745a1 | -12.5616 | -58.35851 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b54c5e19-f7dd-3202-a700-d20139e6dca6 | -13.16569 | -54.86804 | 2024-12-11 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e576b61e-a628-3878-8798-e41325d937d4 | -12.55248 | -58.36938 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 111e424a-88f7-3896-bf3a-cd457ef3a541 | -15.08623 | -59.64504 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b921dcf-feb1-31ce-8489-7796f73ebdb9 | -12.55099 | -58.35662 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdce21f6-6ada-3f78-a863-2d4c432706bb | -17.7448 | -54.21398 | 2024-12-11 04:59:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9a49716-3450-3b83-81eb-898ed4070a9e | -12.53782 | -57.72713 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e8bf1b2-77cd-3e3d-972c-10b8dc91f623 | -12.5446 | -58.35134 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 088f668f-a45d-3c32-b5ad-b24e6ea2fbe6 | -17.74069 | -54.21749 | 2024-12-11 04:59:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ca36d88-88dc-3b43-8386-963f930a7657 | -11.36644 | -57.79503 | 2024-12-11 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6014348-6c67-3fc2-a8d2-39036f2d4980 | -14.81433 | -46.95586 | 2024-12-11 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25c9c874-5dda-3ffa-a2a0-8fb3d4cc45c2 | -14.28399 | -57.46183 | 2024-12-11 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25449498-c517-3a01-a09d-b040fb146c67 | -12.91742 | -55.05254 | 2024-12-11 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42cec8de-7cc5-33a8-959e-6712ccf15ad8 | -12.54281 | -57.73982 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1dfa3a6c-a6ec-3f39-93b6-8c8610353198 | -11.78274 | -55.12981 | 2024-12-11 04:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fa77211-34ec-3165-8c0d-19e3161965ee | -15.09139 | -59.63694 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ff84b64-66b7-3e02-9a2b-9c17ad19ce41 | -12.53718 | -57.73095 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
