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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a6d5d3f-c8f1-3c8b-a82b-3199f2b5b217 | -6.87177 | -45.19094 | 2025-09-17 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6da0909f-75f3-3866-8e7a-e9cbb4e556d5 | -7.58998 | -44.58051 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 250.5 |
| 9b43a291-3f6f-3009-977f-7bbd5887ae50 | -7.66627 | -45.1383 | 2025-09-17 00:11:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d095df52-5b46-3b2d-95d6-27e41365283c | -7.32076 | -43.96352 | 2025-09-17 00:11:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 49c291b3-3e1e-3ad0-a834-2f77e90ca3ce | -12.42707 | -40.92893 | 2025-09-17 00:11:00 | TERRA_M-M | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 51d80c09-cc87-3865-aa5a-85d93aae1217 | -11.43845 | -40.66385 | 2025-09-17 00:11:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9e5de49a-3cea-35ef-b0a5-90d98284f28b | -6.87066 | -43.97684 | 2025-09-17 00:11:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 02546c87-1b07-3dfe-a627-3d4764ecbaf9 | -7.60267 | -47.47296 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0e535d98-589f-37d1-8d69-f870369b3f75 | -7.32539 | -44.06229 | 2025-09-17 00:11:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 612d6081-e969-36cb-8ba8-0784641c3ba3 | -8.98986 | -45.7535 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1978de18-58d4-3ef8-b1e7-dd0b9bb26e05 | -6.35951 | -44.41082 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28f11bbb-1197-3208-a76a-0176a677cb9d | -7.86617 | -48.16453 | 2025-09-17 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5b14effc-29db-3a8a-8fe4-befd629805bc | -7.5773 | -44.55444 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 37fd84c7-6f98-37f0-8568-3edfb85cc572 | -7.25284 | -46.60535 | 2025-09-17 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a202ff73-780f-3269-a472-60594ead20dd | -12.92654 | -42.77536 | 2025-09-17 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3e1f9374-5e08-328d-b20c-3a08ceeaebb9 | -13.65281 | -43.65449 | 2025-09-17 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| af78288f-0d2a-3703-94bb-05621c1d0518 | -7.87731 | -48.16305 | 2025-09-17 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 920ec2fc-d338-39eb-971b-aa80e2b20c59 | -6.97574 | -44.46359 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2c104cd6-4c74-3341-a1e0-aed50d0b5a09 | -11.02373 | -45.06184 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a2f54da7-10e9-36bf-8757-1380435b82bd | -6.51464 | -45.75047 | 2025-09-17 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 1aaa2ba8-6d99-3f58-bde2-f08a05224db7 | -8.16085 | -46.75536 | 2025-09-17 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 795d36bd-fc0b-3a77-9dd7-5912b6e951a3 | -12.36873 | -43.21309 | 2025-09-17 00:11:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 30d80a0f-c096-3211-816a-1af26a4c9027 | -8.63059 | -46.4444 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 6503ce0d-458a-39f1-8c29-c770ec384dfc | -8.97132 | -46.01264 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 71d54d3e-a66c-35a5-8c30-34859d40daaa | -6.34324 | -43.15793 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 651fb6b9-8fdf-34d6-a520-b90e71c09590 | -6.61972 | -44.2922 | 2025-09-17 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ef4ad153-562e-3ac4-b107-b765ce2743ba | -6.68054 | -46.30108 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 2712e924-cf3b-3ac7-b4e5-f02a096289c3 | -10.73484 | -46.54266 | 2025-09-17 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 61293b42-7788-35f4-9266-7b9432dc2be8 | -8.68446 | -46.38411 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cbc2b880-8619-30a5-b36d-d79e0c5e8a6a | -6.62127 | -45.58014 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 155cf1ae-0d6c-3a0f-a3c1-259de4cbcab8 | -7.48112 | -46.09538 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 40038a74-0ffa-32c8-8cce-dc287e44ce8b | -11.03879 | -42.25922 | 2025-09-17 00:11:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b0e571f6-afc4-322b-84bb-6a859a8880c7 | -11.02396 | -48.91817 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 8c2010ed-0150-30d6-9eea-1311abe7984e | -7.59123 | -44.58962 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 233c1dce-c0a5-31d1-8d34-c706fcaca70c | -6.39694 | -43.34929 | 2025-09-17 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8ef3da6a-032c-39fc-a31a-c63f9b1ffa39 | -7.56962 | -44.5648 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2191bfcd-464b-3864-96cf-16fb11032dd8 | -7.00064 | -44.57961 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 14d6a05e-fba9-3aa0-bd76-05be7424cee1 | -9.91187 | -47.6701 | 2025-09-17 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9684e42e-c970-3348-939a-c5566f574e73 | -9.05779 | -44.87716 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 64ee7031-07e1-3909-a1ac-04c031950984 | -8.56868 | -46.36642 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 96f6e86b-f546-3bbe-bce1-edb4663a2638 | -8.15079 | -46.75676 | 2025-09-17 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 783151ff-9648-3df9-9fc1-3d3fbe68e4f1 | -9.10336 | -44.939 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 295f3bfa-60ec-3b10-a8a2-d0530cad5408 | -6.0368 | -43.13803 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 871b6902-ccf3-305f-ae44-cbc354f8e728 | -6.88095 | -43.96907 | 2025-09-17 00:11:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| ab60ccbe-f10b-31ae-be50-9294d287af0f | -7.58104 | -44.58176 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 334.9 |
| 86f19a68-4e9d-3715-a1e5-5bf6e022b9ce | -7.58229 | -44.59087 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 0b1ece59-2a79-3f28-af0b-7a213105504e | -6.23727 | -43.18799 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 931e0935-ab25-301a-8467-ee40b8e041e6 | -13.62662 | -45.37419 | 2025-09-17 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 47659171-598c-3148-a431-5fedd0055f2a | -6.86944 | -43.96801 | 2025-09-17 00:11:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 628a5998-f7d2-3bcf-b2ce-8e2973df28c8 | -9.13171 | -48.11182 | 2025-09-17 00:11:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 13d5a44c-f532-3476-90ae-d423cda2d0ab | -8.91538 | -46.28346 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 07558ec9-3ca4-3467-8a1e-943e00f58c01 | -7.89039 | -48.1762 | 2025-09-17 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 8d2e7a60-4b80-311b-b650-aa5b950632f8 | -6.28961 | -42.38247 | 2025-09-17 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f7b6d936-265e-3a2d-8a1c-926a36bd5cb8 | -8.69607 | -45.8721 | 2025-09-17 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4e0f2e25-7a04-328e-a003-bdb306726452 | -13.33142 | -43.10974 | 2025-09-17 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c5a98268-6216-3bbe-ad7d-3d7eb52f37de | -12.91895 | -42.78564 | 2025-09-17 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 7f48512a-8089-357b-9b24-a4aa54089824 | -6.25103 | -44.68726 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3458beaa-9d70-368c-ba9e-ba263db7e3a8 | -9.07716 | -44.95239 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8b395a3a-94bc-371a-be03-f158b17c8d34 | -8.96161 | -46.01384 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6fb5ee49-c31e-3ddd-ac27-477e3925fab2 | -9.55025 | -46.29465 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 010cc4f2-4880-3775-b723-077f25037579 | -8.95171 | -46.31908 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6ac0505f-31e3-310c-917a-1a0e01e6a20a | -10.69898 | -46.49099 | 2025-09-17 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f99c3973-c0c8-3290-8dd3-4a9ad789d0cc | -6.92162 | -44.81005 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 04b79bf6-4caf-38f2-987f-d9e6daadf6e3 | -12.13547 | -43.18482 | 2025-09-17 00:11:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d5684cf2-d311-37c5-a124-7f10cc208a9c | -12.72735 | -48.02654 | 2025-09-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b5df57b5-6a75-359d-930c-ac923f62094e | -6.95276 | -42.44127 | 2025-09-17 00:11:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| ca49158a-41e9-39dc-b76e-ae8c96ce7362 | -6.97667 | -44.53685 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 462df68a-2e1c-3acb-968d-91eb8073a5d3 | -13.1833 | -44.48284 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ad37ab5a-8cd9-3e73-869f-caaaa6e10090 | -12.91772 | -42.77664 | 2025-09-17 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 740e7f8d-76b1-3272-8a4e-1356ddc4bf53 | -13.8608 | -44.89249 | 2025-09-17 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bdd479de-2217-3cdd-ace1-639bda302285 | -7.25139 | -46.59421 | 2025-09-17 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| cbc5ec4c-5570-32e6-b0be-d0d2cc9ba1fd | -6.61341 | -45.59126 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8732a4b-7a01-3e4a-8ceb-06bf4687c4d4 | -9.74244 | -47.86882 | 2025-09-17 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 31d27001-8b11-3075-a375-079b04f0c768 | -8.15926 | -46.74349 | 2025-09-17 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ff70ee1a-326e-3ca8-97eb-e259181fa1b6 | -8.92037 | -44.47169 | 2025-09-17 00:11:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0908a49a-3b52-3664-bb80-fb16b6067fe6 | -8.93185 | -44.48891 | 2025-09-17 00:11:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1552c43a-f172-34c0-b5a9-b78c97a5060d | -7.32199 | -43.97237 | 2025-09-17 00:11:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6af04bdb-1602-3e30-927f-d7f603f859ec | -12.13424 | -43.17576 | 2025-09-17 00:11:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8016eac8-a030-3cc7-ad10-008333fcc01e | -8.66841 | -47.11536 | 2025-09-17 00:11:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1597cfe9-4c46-3b3f-bf83-f3a111b42d9a | -5.74202 | -39.76322 | 2025-09-17 00:11:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 2b8b813a-662f-3c6e-815f-22e5bfa2c73e | -8.52484 | -42.86996 | 2025-09-17 00:11:00 | TERRA_M-M | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 14755375-4975-3518-92bf-2d26c0ce9b2b | -7.56837 | -44.55569 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c6af2a8f-b1cd-35c4-b64f-c8473d5e683f | -8.53827 | -48.97196 | 2025-09-17 00:11:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3630c498-2939-3402-800e-ba916a0732a7 | -9.10206 | -44.92938 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 4cc4cac7-9445-3f1a-b9f1-0ada80df45bc | -11.50554 | -43.70502 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6376c7af-1861-3f27-b242-3fb4e207794e | -6.97451 | -44.45462 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c5e057a3-677b-39a5-a0ee-5cf1cfdbee8c | -11.4488 | -43.55432 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 580f3610-8b9b-3841-8fe5-a70736fbf530 | -9.08633 | -44.95112 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 76eab464-1733-37d3-8c83-d0352b773dbb | -6.41066 | -42.65567 | 2025-09-17 00:11:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| fc991d74-9ec4-3864-b944-25519e9fc10b | -8.67712 | -46.41494 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 90936ba7-2cf4-35b5-8401-eae2bcce7b73 | -7.84062 | -43.85342 | 2025-09-17 00:11:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 298d3e35-5dc2-36c7-8382-898f422b5660 | -6.61207 | -45.58146 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f03f82c-a389-374a-8f12-e85c8a8c361f | -11.02506 | -45.07201 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| caee853a-9ecb-3c88-9f32-4dad12d8148f | -7.61852 | -47.46513 | 2025-09-17 00:11:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 43059a92-af43-34eb-b438-e41dc775d404 | -7.07079 | -44.35298 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b02be15e-4124-3b38-989f-bc63563510ea | -13.16708 | -43.32415 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 931e69de-303f-3600-be0f-5d15a561fe7a | -13.85939 | -44.88158 | 2025-09-17 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1d7a4cf8-0df2-30ee-9772-a92a25d7da87 | -11.50679 | -43.71423 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 344e2de7-5ac4-3a6d-8799-05d1f6bb7732 | -6.6675 | -45.51859 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e08d8fa8-e6d2-3782-9c2c-55a472a068e4 | -6.5226 | -45.73946 | 2025-09-17 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README4.md)
