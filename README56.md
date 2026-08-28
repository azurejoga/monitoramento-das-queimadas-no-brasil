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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 284e2ea5-fefa-3639-8d16-2aa7e6d111bf | -11.65784 | -46.73479 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e60a5940-b504-344c-ae13-cd371ef9438e | -9.20266 | -67.77894 | 2026-08-28 05:12:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ef901a9-f27e-395a-b8b7-b70067227c72 | -11.1996 | -51.24709 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d000394-7dc9-3d2c-b685-938969dbb463 | -11.76492 | -54.518 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc25b034-2e4a-3dc8-a9bf-e6862c0ebd68 | -10.88497 | -50.52097 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 740ec517-9a7e-3f16-95db-05473ce3108a | -13.58922 | -45.77768 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95cbe539-6265-3f44-ba53-2a9859b46da8 | -11.20313 | -55.08825 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bc8ee16-0bc1-39e2-9c85-a68aacf99d95 | -14.89229 | -56.32528 | 2026-08-28 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75abe461-c5ee-3491-91e2-eaecfa772d79 | -12.26424 | -50.58459 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12888229-4d39-35b5-87fe-d593d6f7ceca | -11.73192 | -54.54585 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b8bee5-7312-3d97-a1e6-336cceaf93e0 | -15.83841 | -56.45611 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3e1fab5-cbf7-3b9b-91c8-dbd016a1d199 | -13.40828 | -51.41076 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e3a38e5d-24b0-3859-b3a1-ae41e2c309d1 | -12.91135 | -59.89189 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf6589ac-6031-38d2-8441-7c10b5f42737 | -11.73371 | -54.53381 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dddb7f82-ce99-309d-bacd-909d571acf7c | -14.86292 | -52.61991 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce8db7af-2b35-39ff-805b-a084c23c2854 | -14.61086 | -47.98536 | 2026-08-28 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f3de9ba-aee7-3efd-be5c-3c5c826ee07f | -11.62392 | -54.59128 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae8fa87a-4ea8-3dab-a447-43e46c95b916 | -9.87285 | -60.26279 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50673369-cc42-3c82-bb01-8d0511d9e52a | -14.93532 | -52.60318 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a26197d4-fa66-305c-a30a-2ca7386937a4 | -11.48438 | -45.07613 | 2026-08-28 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77388410-603f-31f4-ac54-d908a48e46e9 | -11.27068 | -54.02604 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c106037-cc3e-3ade-a837-70aa22d82d98 | -14.89388 | -52.60154 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d135f70-b755-36a9-80a6-fd8a0834d06f | -12.01756 | -47.1636 | 2026-08-28 05:12:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cebb8d03-3a50-353c-8dd6-1040d08fdb06 | -11.20493 | -51.23968 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| cfa0d455-c498-3d7e-b86e-27901c6b35d1 | -12.77516 | -46.44761 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7a70667-405f-39f2-8199-fa49c207da55 | -11.20543 | -55.09635 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e10227a-6cab-36a0-ae95-0e19994f0f58 | -13.60803 | -45.78061 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb8a934b-67fe-35c1-8dde-7d6b13afbb3a | -11.33452 | -48.38296 | 2026-08-28 05:12:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcd03a49-4926-36d0-92a9-28a1fde59116 | -14.96181 | -52.59231 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 618a78d7-877a-3bd9-8a95-28c98acf295b | -11.27847 | -54.023 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e7d6c0b-3512-3b53-a7f2-6692c2467623 | -13.59868 | -45.77761 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbb91b2f-b543-305f-9f35-ff2502feb010 | -11.19752 | -51.23046 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| a78043c9-db4c-3862-b6d5-d4f84377305c | -14.88274 | -52.59686 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5cbb59ba-3665-3b0f-9f8a-633b30d1ab6b | -12.912 | -59.88795 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3e5103b-022b-3db2-b6f2-e94dbdc47684 | -11.23779 | -53.99969 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0d52f1cf-dc26-3284-9ad6-4eae00924d94 | -10.91098 | -50.52913 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75395b9a-b948-3ab4-986b-413bb1c7cd3e | -8.87607 | -66.90276 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aa5a9648-5c0a-3da2-bdbf-7d300da0c050 | -10.75581 | -54.04386 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f7bd53e-b73a-302a-accc-ea4eba389be6 | -11.19913 | -55.09153 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4174c4a3-2e4e-3273-91a0-425349adac85 | -10.92811 | -50.53602 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 094a72e2-ef63-352f-9aac-78b9a2e9d30f | -11.8157 | -47.21338 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58aad070-63e2-3cb9-b45b-7b2949c39fbf | -11.83016 | -47.21911 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c9f4dfc-a1af-3af7-b021-6eb609793131 | -10.89384 | -50.52222 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 220a2f63-b770-33b3-a996-21ca33fd5d22 | -10.91985 | -50.53037 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4126cf0e-7204-3ba8-b385-19b9188d65b9 | -14.87266 | -52.63975 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b6851d9-6b2a-3721-9f05-0d03ac7ed6af | -11.27724 | -54.03133 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd590b05-41e3-3a40-8e68-f9302b94e20e | -14.98894 | -52.60744 | 2026-08-28 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ac0e66c-582d-3b1a-b849-2cdcf33b9157 | -14.29849 | -51.7301 | 2026-08-28 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14c2b2bf-ddd2-3afa-af7a-191db9cf8918 | -11.65045 | -46.74231 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 683efb93-b8bb-3503-aac9-a2f9e7caf19a | -14.97458 | -52.59042 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d007aba-a135-3e02-969d-daf37773b35f | -14.6105 | -47.98239 | 2026-08-28 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331f1c95-8e76-3e1b-8979-e25e4a665edb | -11.2312 | -53.99447 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdd88fef-1aef-3035-977c-60cac061360e | -11.72606 | -54.53675 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad7d6269-7a21-36af-b292-8a3f1a81b34a | -12.7835 | -46.45391 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a36c024f-d098-3782-90cd-587fe5135a40 | -11.01933 | -49.65584 | 2026-08-28 05:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84c8f133-c82d-31ef-9988-ad667de54900 | -12.25874 | -50.57631 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b2ebf8c-1e19-3aa8-b856-5b66bbce10b1 | -14.45388 | -53.34747 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca64983d-072d-3f5f-8d76-9a02e6b858bc | -11.77166 | -47.65789 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2650df1-4c6f-3ab9-abbc-f95ccc95e99d | -14.49453 | -53.40556 | 2026-08-28 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a42fe5d0-503a-309e-a44c-186d01ae60fd | -11.20724 | -53.9966 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84ca2ac9-b7fd-3f92-b632-e9a4f29fd2c0 | -11.82179 | -47.21043 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ea869e2f-77a2-35f3-aad0-1e32a6cb9a2b | -10.78816 | -61.41865 | 2026-08-28 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa48fd70-9ae6-3225-a500-a09c78b299f5 | -11.206 | -55.09256 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b5dbee7-33b5-3ebe-a89a-8789b7e82cb8 | -11.73545 | -54.54639 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 395fba08-cf61-39d8-b193-e95f601dbcd5 | -14.41539 | -52.58872 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f2d46c2-5a13-379f-834d-83ce38615423 | -14.45096 | -53.34863 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e3c5e11-a2bf-36b0-af73-1cfe98947348 | -11.22458 | -54.00351 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb14c6cd-578b-312d-a5cd-5eec826d16ca | -8.63318 | -66.53506 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0116b3f-1b0e-3bc4-8fd9-9a84695286dc | -11.81938 | -47.21378 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 080f7785-b541-37f8-b23f-1b5a42f2c9cf | -13.42828 | -54.0192 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee81c682-f6be-3bc3-8737-a0506c71729f | -8.99232 | -65.44029 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5a44332-5c3e-33bb-8e39-09ccc3da1b29 | -10.50576 | -64.51357 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1ac32a61-7c94-3b72-8951-4813e7051768 | -11.20863 | -51.2443 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd60a4d7-e880-3de7-9b97-1d4526acec05 | -14.90971 | -52.60781 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0b6db44-7088-3154-bd2c-3477d5f89b40 | -10.80119 | -50.64434 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59624473-8f83-36ba-950a-48bc12b33f1e | -10.77602 | -50.632 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94189b3c-97c7-39ae-bd6b-2892d84942b4 | -14.18734 | -52.82739 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4950a068-1cf8-32c2-a898-89500274e4f8 | -14.39865 | -53.05445 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d36030a1-c941-3439-b852-5ea9b8cc4178 | -11.71315 | -47.80325 | 2026-08-28 05:12:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b84c892f-dab2-3179-a9a7-c6d63eb0e7ce | -14.4266 | -52.59756 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c6d1feb-13df-3c05-a928-15202e0f7b69 | -12.2429 | -50.57227 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86f78904-531e-39dc-8dc0-f1eaad6bacd3 | -8.63878 | -66.53612 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12349600-679c-30d9-92a2-4585fcca73c1 | -8.99691 | -65.44445 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97446029-d71e-3419-8a53-5101f0a81db8 | -12.50393 | -43.8096 | 2026-08-28 05:12:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fb3aec11-b858-3a96-94ee-119e21ac92e5 | -10.79771 | -54.00817 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af74a232-a514-3706-8852-12d20538112d | -12.23621 | -50.57321 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88636d85-eaf6-3cc0-9750-88ead914eb05 | -14.89026 | -52.59735 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79dedb7a-e558-38d6-9580-b13434c62536 | -11.27191 | -54.01769 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b83ba44d-e605-3ed6-bfbc-22c9bc929e0f | -10.77255 | -54.02958 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 757399a7-45c8-3860-b301-103bdd823013 | -14.93579 | -52.59967 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 15587216-6dc1-3dab-8d93-5e2e9972d151 | -12.24522 | -50.57445 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04ebe9c3-6893-3e09-bb6e-112ae4a7208b | -11.64464 | -46.74181 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 337672ec-a7fe-3bab-8f71-44a9f25b32f4 | -10.26634 | -64.50085 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ec6b14a-15cf-349a-98d6-d4ee411418ce | -14.87816 | -52.59983 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36c1a9c3-f648-3c33-9bcb-63d5aec4769d | -13.40885 | -51.40654 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9d3aa7c0-9a1a-3012-971b-b5d0d33fcc7a | -9.20392 | -67.7828 | 2026-08-28 05:12:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d1332b3-4457-34af-a175-15c5b03eb6ce | -15.77039 | -56.4453 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ee394cb-c2c0-3863-8f03-6deb57728723 | -10.75999 | -54.04031 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1472170-2721-3a6d-85b4-975974ff40a8 | -8.86884 | -66.90968 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ad90712-8c9c-3c22-8ce0-84f07dddd92e | -11.72313 | -54.53222 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README57.md)
