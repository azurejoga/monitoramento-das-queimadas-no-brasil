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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ab3f49c-18fb-36df-a298-9e758dcb70eb | -5.76643 | -43.49204 | 2025-05-23 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7d71760-abda-35ea-a732-569cc4050e3b | -6.03461 | -44.05312 | 2025-05-23 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de134a16-9d95-3d3a-9e03-a48b649058e2 | -7.06564 | -44.93775 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4eb033c5-5b1d-3941-b668-bda439d9964e | -6.94724 | -42.79824 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b01594ba-a4f8-3608-8a7d-3ac3be53df7a | -7.07269 | -44.93322 | 2025-05-23 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 61e9481b-713f-396c-ab1d-62e44a19e2fd | -6.9426 | -42.79671 | 2025-05-23 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ea3acd9-a59e-3a86-b415-d447f30b5908 | -5.9735 | -43.75631 | 2025-05-23 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34039bac-c449-34d3-9b70-268676be19e7 | -17.09639 | -43.80585 | 2025-05-23 03:38:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1b70a20-0e7f-311d-8e86-04b00d9f3d1d | -11.78066 | -44.28191 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90cf8d10-14d1-3bac-96d1-3851fdb7819c | -12.0746 | -47.34055 | 2025-05-23 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6716c3f6-3b92-364c-a3bb-d06ef82b4b21 | -11.78131 | -44.27847 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5baaf192-fca5-37a1-b510-da34539fe6ca | -11.55354 | -47.44785 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a6eb2a3-f94c-3ba0-af80-08661af4f9c8 | -12.40949 | -42.52887 | 2025-05-23 03:38:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f7f76c01-b16f-346b-97e4-ef782d5f0ca1 | -11.97106 | -44.15908 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83bc88f8-0f4d-3358-9eb6-0a4b9838c53b | -15.426 | -41.41251 | 2025-05-23 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4156fb8b-a723-3b73-99a3-6ab4f4e28a00 | -12.17838 | -40.3503 | 2025-05-23 03:38:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| baf09040-ca1f-3cfd-ac2b-f43d2a55532e | -12.06706 | -47.34475 | 2025-05-23 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 55200734-5867-3398-9052-bf81669a490d | -14.67799 | -45.11124 | 2025-05-23 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 460d4f3d-6b20-39dd-ba7d-911e07c78a0b | -12.07349 | -47.34594 | 2025-05-23 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7717e6a-494b-3e65-9c3b-ab90da10b52d | -11.56655 | -47.45049 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49ae02d7-50f5-31d7-bdb5-0f9bb8ae3fc6 | -18.55285 | -40.06544 | 2025-05-23 03:38:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e15b886a-ee0a-3f34-b1c4-88501c16ec5c | -11.9389 | -43.93119 | 2025-05-23 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 952a1667-efc4-3cd4-9e89-b896426970e1 | -11.78387 | -44.28271 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 58adfd1c-16dc-3b95-8deb-ac78c91f16be | -14.20527 | -41.85778 | 2025-05-23 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5e1ea1c-6322-3e9a-a76d-6b1565bc9658 | -11.93753 | -43.93526 | 2025-05-23 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34df7407-cc2c-31fd-92ea-d2da8a86697e | -14.8728 | -45.12362 | 2025-05-23 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dd212c9-f3e6-309c-b055-e7a97c0121e6 | -14.87348 | -45.12016 | 2025-05-23 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa82d766-0ed7-364b-bcbc-864d6e267cf4 | -11.56541 | -47.45597 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0fa1288-a415-3661-8ee2-cb61e79b582f | -11.97171 | -44.15571 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4627f10b-c2f4-3b59-a37b-83a5e6b491e5 | -10.49364 | -42.41724 | 2025-05-23 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 780ef19f-0db1-3eb3-929f-8c391a708f13 | -14.67869 | -45.10776 | 2025-05-23 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d259541f-e612-3a27-9862-1fb11435a3c0 | -14.13623 | -41.69044 | 2025-05-23 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3ff31b4-165f-3abc-bb7a-cb554c8960a7 | -11.51362 | -48.55548 | 2025-05-23 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1bac07c-3b72-3722-9269-9f227a763737 | -17.60213 | -42.83802 | 2025-05-23 03:38:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfa2acc2-cd76-34c5-8812-8312199586c9 | -11.79389 | -44.28811 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f5631d57-8c90-3d93-9106-290c52f9833b | -18.54995 | -40.06213 | 2025-05-23 03:38:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1d1efcc2-1f02-3a39-8950-b7725060f9fe | -15.42188 | -41.41165 | 2025-05-23 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9eec6b20-a8a2-3856-88f2-1a3f0d1246be | -11.79323 | -44.29156 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d2cbdc9a-a176-3f67-ae72-db0a357b7d45 | -12.85251 | -47.39244 | 2025-05-23 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c49f434e-2010-3fc0-be32-2e52a06e63b1 | -12.06591 | -47.35029 | 2025-05-23 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7864b005-c102-3ab1-aa95-dfb84d0bcdc9 | -11.78855 | -44.28713 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 070032b9-e4e0-3aaa-8513-6b6a758f2ea6 | -14.87084 | -45.12315 | 2025-05-23 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3890294-3025-33ae-ae5e-d2888a6e8bee | -12.07991 | -47.34719 | 2025-05-23 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1251b87-eb35-3e2b-a903-91fafecc0186 | -11.55774 | -47.46021 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68d58ee6-3e93-32c7-8997-fc748ba91e37 | -11.78454 | -44.27929 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a36c7761-4cd2-35de-886d-70f0cffab321 | -11.56008 | -47.44902 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfb2acc3-1bba-3953-a3cd-1c3a6386e154 | -16.71363 | -43.22749 | 2025-05-23 03:38:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ac54dff-8461-3b00-ba1d-d2f265d0e811 | -11.93827 | -43.93444 | 2025-05-23 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9109bc1-fa8d-3002-8b4c-bbaeb468dae0 | -11.78321 | -44.28614 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5c463621-b332-31f7-ab3a-610b9bde96cb | -17.77983 | -42.8117 | 2025-05-23 03:38:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82a02038-2f21-30f9-af22-7f34fe7b43d4 | -11.56673 | -47.45218 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0df0a3fd-4c22-3dc7-8dc7-a30f8d347095 | -18.03925 | -39.92506 | 2025-05-23 03:38:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 686020d0-dbf7-3a5b-99a9-6fa8337cca9b | -15.42257 | -41.40786 | 2025-05-23 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ef4f5e90-5c1b-3615-a91b-111d053bc8ff | -15.74738 | -43.48756 | 2025-05-23 03:38:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e80850ea-208d-3a03-9e03-c62ae40c13f0 | -11.55374 | -47.44945 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f497758b-15ba-335c-b40d-7be7773671e9 | -14.87154 | -45.11971 | 2025-05-23 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eff35fbf-9859-3e37-9c67-434f780cfc45 | -11.56026 | -47.4507 | 2025-05-23 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 538dc1f0-af26-3592-a900-16eaf064e1f6 | -12.84728 | -47.38574 | 2025-05-23 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e60cecde-1522-362f-a377-01941f9c31cf | -12.07877 | -47.35276 | 2025-05-23 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f9d38cf5-9c70-3c01-8ee5-b1ef81e982c6 | -10.48881 | -42.41636 | 2025-05-23 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9d4f001c-eb26-3d9e-baaf-1bc4b62aa4ed | -12.83879 | -47.39486 | 2025-05-23 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa616382-f287-3f1d-98ed-7aea39160fc5 | -11.51222 | -48.5622 | 2025-05-23 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8a64519-0d84-3363-af2a-4c59d96a0887 | -11.78988 | -44.28028 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d8136a61-980b-3d32-852b-f25f5ffe14b0 | -17.59636 | -43.19999 | 2025-05-23 03:38:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62330868-36c1-3f4b-b2bc-f1de9abcdf16 | -11.93814 | -43.932 | 2025-05-23 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9953d49d-2910-3e82-80aa-edebe3d74f26 | -10.49509 | -42.41571 | 2025-05-23 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 251d3b16-1a2c-30f5-8f22-13d4f8751e55 | -10.49464 | -42.41186 | 2025-05-23 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ab96223-1eb4-32c7-bc61-eb05cc34c51b | -11.78922 | -44.2837 | 2025-05-23 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e95b609a-e2be-3e18-b2f3-dd458f6c277f | -12.8462 | -47.39101 | 2025-05-23 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e020115-e892-30f7-9262-7161952f9bca | -10.49413 | -42.4211 | 2025-05-23 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c1a1314-3b0b-3d4b-b3b2-ec0982b8a702 | -12.06817 | -47.33933 | 2025-05-23 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4255bb7-c9f1-3ffa-8e07-ec570e24239f | -11.56961 | -47.90165 | 2025-05-23 03:38:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd46df4f-d7fc-39bf-ae0f-3719045b02b9 | -10.49026 | -42.41483 | 2025-05-23 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b72698c4-7162-3dd7-93b7-24d398d5daee | -14.001 | -56.0131 | 2025-05-23 03:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 398cefe2-f960-36bf-ba97-7946b06eb13a | -13.9818 | -56.0151 | 2025-05-23 03:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cbe7f99d-4c5f-3c14-b6af-42fbad2be081 | -22.78753 | -43.75629 | 2025-05-23 03:40:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d346edc7-b5fa-3764-a81f-528db1d286ea | -19.16785 | -47.70027 | 2025-05-23 03:40:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c5f2294-c140-3eef-b55c-82bdc5ffd9d0 | -19.17361 | -47.70151 | 2025-05-23 03:40:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c5c1658-f377-3075-bc04-fad61b8dc2ef | -17.91287 | -45.53188 | 2025-05-23 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bca79ae6-7ffd-3ed9-8822-292ebb42f086 | -22.6778 | -42.85502 | 2025-05-23 03:40:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 0b52a723-9810-38a4-992c-724961f80db7 | -22.78045 | -43.04422 | 2025-05-23 03:40:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c3fb8d7-5f9b-3039-ac10-441399ae432f | -21.62693 | -43.46612 | 2025-05-23 03:40:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 05fcb83e-5010-3998-9e18-bf0d0fb1971f | -20.0672 | -42.24522 | 2025-05-23 03:40:00 | NOAA-21 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d9de7121-16eb-3f99-b5ba-0fcca4010e71 | -20.06648 | -42.24905 | 2025-05-23 03:40:00 | NOAA-21 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36b9b9fe-1c42-35c4-902b-586d6f9efa9b | -19.45469 | -45.30768 | 2025-05-23 03:40:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95db62a1-4b28-35a6-a3d8-700f30e7819a | -17.68247 | -46.82529 | 2025-05-23 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e224f3b7-d3c2-390a-bbf9-5e4970d30dc2 | -21.62737 | -43.46631 | 2025-05-23 03:40:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cfdff749-931f-33fc-9e77-8383a40bd37f | -22.53848 | -48.81152 | 2025-05-23 03:40:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66838530-c17d-3e56-ad87-b1214b3b88ff | -17.6799 | -46.82318 | 2025-05-23 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a79cc9c-43f2-33d3-b6d6-046b9fb977d9 | -18.33644 | -45.59242 | 2025-05-23 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7985f615-fd9a-3457-965c-5c9982e4f394 | -21.63182 | -48.34246 | 2025-05-23 03:40:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b541d45-0454-36d1-a410-6b0ded3faf60 | -19.83752 | -40.08128 | 2025-05-23 03:40:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a05e8aff-8d88-3a59-a39e-66bf48815c47 | -14.001 | -56.0131 | 2025-05-23 03:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 298a6d51-e3a2-3669-9be1-e58f514065d1 | -6.2224 | -43.3693 | 2025-05-23 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2e04951f-f3fa-3129-be58-f0f57e7a2d6c | -13.9818 | -56.0151 | 2025-05-23 03:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| bd2de926-b20b-3ac4-bf01-c893fe5767e5 | -5.5876 | -45.2091 | 2025-05-23 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| e5f56c84-e2ed-3de5-bd74-991406cf1a5f | -6.2224 | -43.3693 | 2025-05-23 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 34fa884c-2fdb-3af6-8b77-cd7c1a9e4b00 | -7.0695 | -44.9335 | 2025-05-23 04:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 558f4d99-9b57-334b-a590-9b147c153c70 | -13.9818 | -56.0151 | 2025-05-23 04:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e902845c-8a14-30da-8bbd-a84215cbf322 | -6.23257 | -43.35755 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README7.md)
