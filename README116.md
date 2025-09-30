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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a7e2f6f-8bc3-30c4-b232-c317f19ff663 | -6.523 | -45.207 | 2025-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| e2709b8c-9685-3f51-bde5-5555a84394be | -10.0342 | -50.1997 | 2025-09-30 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| bc96c02b-b16c-31b9-afba-0e60ec7c2e2c | -5.2869 | -43.1613 | 2025-09-30 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d64ec62e-03c9-3408-adc7-b500d3b7ac0a | -8.541 | -44.6515 | 2025-09-30 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| fb444fd0-e444-3e42-90f0-22a0c5068722 | -7.2807 | -42.8741 | 2025-09-30 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 96c29e06-e309-3a49-ab70-67b7a6b03604 | -8.8229 | -46.189 | 2025-09-30 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| fadd2bf0-79b0-3510-87a9-8a763c108d87 | -9.0425 | -46.7032 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 71912164-16c4-32b8-aeb7-f3a99de12d85 | -8.8732 | -46.6762 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 14f62d95-af6c-3fa7-9963-f757c8b4641e | -7.938 | -44.6226 | 2025-09-30 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 1fa2cd43-dfd3-3a7b-96ec-a798479a9230 | -14.5133 | -48.4745 | 2025-09-30 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b5c83904-7c23-39f0-ae7e-7a9d8026a6a5 | -7.8188 | -46.7783 | 2025-09-30 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 203.2 |
| bc0dc0c7-3e8e-34d5-8fa6-95de09e9a28e | -7.2999 | -42.8486 | 2025-09-30 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 39553b3b-84b9-35f9-9908-a306d61bc148 | -7.0507 | -43.2255 | 2025-09-30 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 032a7f46-ceaa-314d-94e9-f36069a37d99 | -9.4194 | -54.697 | 2025-09-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 7d1abc73-700b-371e-82df-a234b0e7b5f2 | -5.475 | -43.0774 | 2025-09-30 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| bd957d3f-d065-3f2d-abf0-53486f80bf47 | -7.0319 | -43.2273 | 2025-09-30 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 42f265b2-2faf-379a-b08c-6a6f9b168178 | -12.9524 | -48.3963 | 2025-09-30 13:40:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 40f17e9f-56fc-3902-9a3b-8fb1a6eaff53 | -7.115 | -47.785 | 2025-09-30 13:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 447d4049-f349-341b-812d-a842aa0aa269 | -11.1944 | -47.2334 | 2025-09-30 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| de4f1328-e350-3ee4-a12a-f58175f5cda0 | -10.0531 | -50.1978 | 2025-09-30 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| bf2caffd-2430-3001-a3e9-99e29a40eb81 | -18.218 | -53.2962 | 2025-09-30 13:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 42a7daa4-12f8-3a4e-b5d1-20fca6cc8252 | -8.2662 | -45.5018 | 2025-09-30 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5f8d22b5-e5db-3e48-996a-b38114ca8858 | -12.2153 | -47.8112 | 2025-09-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 42f1d4c0-6e96-3401-9241-bfeba3bde955 | -5.2867 | -43.1846 | 2025-09-30 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8dc4b0eb-2b61-34c1-9c23-38ddae446dc0 | -9.1248 | -47.6256 | 2025-09-30 13:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 0f23b2f8-3e1d-3844-b581-a8c29d53c92d | -10.1234 | -47.783 | 2025-09-30 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 78abc070-4881-3aa8-91da-2cbb637b47a4 | -14.6603 | -46.9663 | 2025-09-30 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 14c53f22-6877-3c21-8a1b-698aa079531d | -5.8646 | -45.5958 | 2025-09-30 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 319a9dc7-a521-3247-9012-47d7f6d1281e | -5.843 | -45.934 | 2025-09-30 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a5e922e5-efb7-31d9-bc72-eb37fe725c90 | -9.4005 | -54.7186 | 2025-09-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 35cef6bf-fb01-32e3-be66-23e7d00f886e | -14.5323 | -48.4938 | 2025-09-30 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e5caadb3-eff5-3f9c-aa20-e21c36ae9b4d | -7.9191 | -44.6245 | 2025-09-30 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 16a436b5-604d-3aea-b733-c7427b92568f | -12.7022 | -45.2715 | 2025-09-30 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| d9273bab-411d-3646-9044-268e8f9e6245 | -7.2996 | -42.8722 | 2025-09-30 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| cd76ec14-3956-3294-b2c1-4caa65e473f6 | -8.672 | -47.7144 | 2025-09-30 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0cbb2447-3395-33fb-bfdc-7e29912aa5a2 | -9.4007 | -54.6984 | 2025-09-30 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 7b010742-e2fb-3953-ac3f-8b6dd3728747 | -17.921 | -57.5952 | 2025-09-30 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| efdfc9e5-c824-3d93-9137-52ebd2976e5b | -14.7171 | -45.2291 | 2025-09-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| fb13bdfb-e844-3670-8739-703254167456 | -10.0717 | -50.2173 | 2025-09-30 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f10910aa-2c12-3638-b4ce-887ebc11306c | -6.5227 | -45.2297 | 2025-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 202.6 |
| 67d920a6-25a8-3792-bb6d-dbcf30d1d823 | -14.5517 | -48.4907 | 2025-09-30 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4130120e-dba5-3243-be96-38ac09d6e1d8 | -8.6668 | -46.608 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3a26d87f-c86c-3e24-a9aa-596ee790f708 | -10.1851 | -44.8939 | 2025-09-30 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 368.6 |
| 422b4ba9-6da9-35eb-a752-5af6311f9237 | -8.1616 | -46.3675 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 2279461c-8e2b-3c66-8e71-925190ceffbf | -15.7719 | -43.6714 | 2025-09-30 13:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 243.1 |
| e86e76dd-a46f-3d95-928f-e5f2ed4061d0 | -10.3058 | -48.2681 | 2025-09-30 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 46f0e870-6b26-386b-a573-3a84e76b6662 | -7.8353 | -46.9764 | 2025-09-30 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 203daa96-3e2b-3a48-a1d6-b845ffa7c17d | -5.7223 | -42.6826 | 2025-09-30 13:40:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 3850e3c8-2e9a-343e-870b-24b84ab85020 | -7.8373 | -46.7988 | 2025-09-30 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 91780cba-1393-3c37-af88-4622f4c9aba8 | -14.6947 | -48.1332 | 2025-09-30 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5f80a0f8-d2ff-3835-a44d-a5b8226ce4c6 | -11.1548 | -54.1054 | 2025-09-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 7c6751ab-320c-3ebb-bbf2-be277b24ba50 | -10.6419 | -48.6021 | 2025-09-30 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 0145145d-3dac-304a-ac8c-c6566cc62e2a | -7.9194 | -44.6016 | 2025-09-30 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 178.7 |
| bd2bd6e8-2d1c-3dcf-8e00-145f4c6bff36 | -15.9273 | -46.2101 | 2025-09-30 13:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 272.4 |
| 1a4c7904-2bb4-3722-8e71-4a599647bfd0 | -5.8428 | -45.9564 | 2025-09-30 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| ec9dbe23-8d3a-3097-9872-2bc8a9dbc058 | -6.2759 | -43.6442 | 2025-09-30 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 43921ada-1d3a-31c6-b04f-983aefcf14ea | -14.7367 | -45.2255 | 2025-09-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| d6998500-0adb-39ef-ae06-228a99076595 | -7.8375 | -46.7766 | 2025-09-30 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 295.2 |
| f4a157c7-d0a5-3983-856f-f79fbbad804d | -9.0236 | -46.7052 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 42e28575-fa7a-3a32-bbca-11a5f819bc12 | -12.2344 | -47.8086 | 2025-09-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 9b242704-779d-3716-a176-272de1f57c17 | -8.8734 | -46.6539 | 2025-09-30 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 80384748-8100-3f56-8eb6-b6bad84dd078 | -15.7917 | -43.6672 | 2025-09-30 13:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 0471de7a-83ad-330b-ada4-56a65716ca14 | -11.6837 | -45.3563 | 2025-09-30 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 20f14177-532a-3545-86f2-4e6a290504f8 | -5.7411 | -42.6812 | 2025-09-30 13:40:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 1883ab00-81e6-369b-a864-8a2b0a8fd9cd | -14.7166 | -45.2525 | 2025-09-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 24c308df-3f3a-3f6c-80a4-9c96b174d4fd | -12.952 | -48.4185 | 2025-09-30 13:40:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| acbfb44a-5b0d-3d8a-95b2-966a5c2b7d88 | -14.5141 | -48.4299 | 2025-09-30 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f462cef3-8984-304b-b82a-0cad41944e58 | -10.0528 | -50.2192 | 2025-09-30 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 79baca3d-2187-3308-a2b2-28271b74efc8 | -6.4131 | -43.0724 | 2025-09-30 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 67b75fc3-d9aa-3184-80b3-048792aab0d9 | -9.9585 | -43.5752 | 2025-09-30 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b0ec61de-0ea8-3069-83d5-436658e6418c | -5.4258 | -42.2797 | 2025-09-30 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 86736279-bd3e-372b-a4e6-9cea764042dc | -7.8348 | -47.0207 | 2025-09-30 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 6934d2b3-06ed-30bd-ae8f-7a983985fb14 | -9.1246 | -47.6476 | 2025-09-30 13:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 1420b91c-9deb-3067-ac83-0666d9626f58 | -9.1434 | -47.6457 | 2025-09-30 13:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 92d78664-7447-318c-aa8a-f42751e921ba | -6.098 | -42.6521 | 2025-09-30 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 9d1a14b7-1a14-324e-a0f3-83f3eb5e6295 | -18.4862 | -44.0191 | 2025-09-30 13:40:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 689724b5-a2f1-3d2a-9f76-cc56228c1933 | -7.8378 | -46.7544 | 2025-09-30 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 1efee026-f495-31a2-b977-6a91eb5ed997 | -8.244 | -45.7754 | 2025-09-30 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| dc4a160d-62b2-399d-9761-44f964a870c1 | -7.5146 | -45.4385 | 2025-09-30 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 1027bb31-78c9-351c-a829-3ff87352cec0 | -12.7018 | -45.2947 | 2025-09-30 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 5adefe73-5adb-3d1e-849a-837c13088e74 | -7.4958 | -45.4402 | 2025-09-30 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 4c1e0344-a331-3830-bba2-b47d7de13689 | -14.3847 | -47.1486 | 2025-09-30 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 178.0 |
| e0c0c9b3-2a29-38f8-8843-8ab15d4bd2ff | -14.7361 | -45.2489 | 2025-09-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| f9066ac8-d528-3e8e-8a23-69bd8b968924 | -7.8696 | -47.2606 | 2025-09-30 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| b2a738ba-d1c0-317b-a70d-0336bbde9ba7 | -5.8616 | -45.9327 | 2025-09-30 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 686c9662-3037-33bc-8fbf-2255af3509e0 | -10.0339 | -50.2211 | 2025-09-30 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ff37d057-3a27-3833-ac3f-df26e1a16a57 | -14.7361 | -45.2489 | 2025-09-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| df368744-6f61-3cd2-8b13-e5b3ee531eec | -5.8428 | -45.9564 | 2025-09-30 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 5b8338a4-7336-3daa-8d14-6eeb5b2f0d7b | -8.672 | -47.7144 | 2025-09-30 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c430a605-4c3b-3463-8175-431bb8169a84 | -14.5141 | -48.4299 | 2025-09-30 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| b9744ebc-69bf-37a8-a894-1546b99ffbab | -12.1072 | -44.2021 | 2025-09-30 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 7abf348b-91bb-3ef5-aeb3-74dae0be3731 | -5.8144 | -42.8637 | 2025-09-30 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| efdfa355-4fa1-3f10-89de-218e217e343c | -10.1851 | -44.8939 | 2025-09-30 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 376.6 |
| 7a7130ee-dad4-3e19-bc60-4faf3634df63 | -6.523 | -45.207 | 2025-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 183.3 |
| ce3e2be5-f1db-35a6-9d67-4aa2e49131e1 | -15.9268 | -46.2334 | 2025-09-30 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 0207d5e9-0c09-381e-8a96-4d2368fc6b9a | -17.9411 | -57.5722 | 2025-09-30 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| 586f3482-4e89-3293-beb1-3427d7817dc4 | -5.9192 | -43.6961 | 2025-09-30 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a45f3c60-c9bd-3566-a677-9749d9cdea61 | -7.0481 | -45.1856 | 2025-09-30 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5bdeb08f-eb53-3822-9f44-2d487ec72fbc | -9.8845 | -45.9576 | 2025-09-30 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 38e720bc-eed2-3bad-8289-4c46a83276e7 | -5.2867 | -43.1846 | 2025-09-30 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |


[Clique aqui para ver as próximas entradas](README117.md)
