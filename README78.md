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
| 33fac42d-f0ae-3ef9-a87c-029091f1c051 | -11.20979 | -47.74973 | 2025-09-29 05:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c12967a3-577a-3f99-afe6-2080141b2b5c | -13.63286 | -48.05684 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f55be8a8-4c9f-3617-b0fd-12f896867d17 | -11.83044 | -51.80115 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4847963-8013-394d-b8ef-6b11349a87e2 | -13.6335 | -48.0418 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 406dae9a-8655-35c0-980d-52739f2a8e77 | -11.8418 | -51.80212 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 7e3b2117-89ac-321f-9c06-18442dcbe830 | -14.54971 | -48.40665 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5b98570-649f-35ca-bfff-52e336e2b4c4 | -17.75643 | -48.77085 | 2025-09-29 05:27:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 830f6d88-c4a4-33af-b621-2ebfe0bc74d3 | -15.2835 | -49.51283 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e23cdf7c-0108-398d-92c4-8f2e46f06871 | -15.21223 | -50.11024 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac116802-da5e-377e-bc8a-e728323ea146 | -15.25699 | -48.77351 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 849fdc40-83f0-3c9a-a942-4d758fd2be93 | -14.55048 | -48.39864 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 144ac544-7e21-35cf-bd78-7ddb6391426b | -17.75773 | -48.76526 | 2025-09-29 05:27:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a42c72fa-96a1-331e-8a76-d302729e0f68 | -11.62274 | -52.86119 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4c5f719-b950-3e52-ae46-a811c8da06fe | -11.84229 | -51.79827 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| fd20b684-bba8-3d6d-82a4-add2cf4e3029 | -14.67696 | -48.1554 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87162505-b999-30d0-b310-46725b9810c8 | -13.2312 | -50.95746 | 2025-09-29 05:27:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 853f3334-073e-3d65-9bee-45061613b606 | -14.52895 | -48.43827 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 75ea2085-ac6b-3108-8303-61c7338ca545 | -15.21992 | -50.10024 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0d4860ab-aa43-325b-8743-c11126634fa6 | -11.62317 | -52.85794 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f32f1c-eeab-3588-b39d-8b4d86b4eb8b | -13.75723 | -47.91845 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c723d55-ed19-352d-bc30-a7ce9cd9fd3f | -15.28168 | -49.5128 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| de6204c3-3d77-3c35-999d-fc24562652ef | -23.22906 | -49.41036 | 2025-09-29 05:29:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| edf69cdf-3e58-34a4-99d2-41c7d29114eb | -23.47571 | -52.09618 | 2025-09-29 05:29:00 | NPP-375D | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c9d2c3c2-b2c9-3a69-b4d3-e7d3e65fe6a0 | -18.20326 | -53.31959 | 2025-09-29 05:29:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff6654a-4159-3426-8da7-f0d4467ea81d | -17.91171 | -57.61243 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 9b530132-a48c-375f-a195-ff54240cc7bc | -18.21626 | -53.30319 | 2025-09-29 05:29:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a01c3c59-6c26-39f7-a62d-4831c57b7bf1 | -18.17647 | -53.30692 | 2025-09-29 05:29:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bce08e15-b89d-3b5e-9842-ab9239abcbdf | -23.22128 | -49.41691 | 2025-09-29 05:29:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 071e39a8-23b2-3cdd-95ff-870241860bf1 | -17.907 | -57.61606 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 17cff8e3-79d1-35e0-b0f3-bd76a4aa4d9a | -18.21036 | -53.30582 | 2025-09-29 05:29:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 63715b97-e29e-375f-a9b4-99acc391d890 | -17.91218 | -57.60878 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 663b7f92-218f-3bc7-8180-565b72d72e9c | -17.90795 | -57.60867 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a0f8c841-5d4a-3e6b-aa61-62d460c30e4d | -18.20891 | -53.31933 | 2025-09-29 05:29:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cca0521d-338c-3edb-91df-da6c4f89b691 | -17.89395 | -57.61865 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b7422ca6-3fdf-3048-bd32-4768455a8851 | -17.89441 | -57.61506 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7d638218-4ed0-314d-b55e-f5d5e2173b64 | -18.17686 | -53.30325 | 2025-09-29 05:29:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55471878-027b-3955-bb23-c8f634787196 | -17.91126 | -57.61597 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1d680e4a-2007-34ce-8d44-8753aaaa2727 | -23.41746 | -49.46229 | 2025-09-29 05:29:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d6821327-aaee-380d-8436-ccdf5a3ada0a | -17.90325 | -57.61226 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ce8a79fb-e0db-385f-a776-a6e918e47164 | -23.22173 | -49.4096 | 2025-09-29 05:29:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 28b989c0-c1b4-3d74-9723-af53110b286f | -17.90653 | -57.6197 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e4cb6050-2444-3ad1-823a-aebbff81affe | -23.22952 | -49.40301 | 2025-09-29 05:29:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 2e2400db-181f-3967-8bb3-b0ea591539a0 | -17.90373 | -57.60851 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f3de5377-ba97-324b-a823-3024f5d6f091 | -17.90277 | -57.616 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| deabb5b1-da7c-30c9-b036-2f47e4943523 | -17.89905 | -57.61196 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 456ca572-646b-336e-9b82-65d71b9763ea | -18.21105 | -53.29925 | 2025-09-29 05:29:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 593d4c2b-00d8-3097-8414-803f806f652b | -17.89811 | -57.61927 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b56590fc-cd48-32da-841e-58e2f2fc51d9 | -17.90747 | -57.61241 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ee6b2c72-ba4f-31bd-9064-f487de02156a | -23.22225 | -49.40123 | 2025-09-29 05:29:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| abb0bf11-90ab-32d6-9e0f-ed3f04f4a4a9 | -17.90609 | -57.62312 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db2da0d4-5b49-3c82-81ad-2e63e622f33b | -17.89857 | -57.61565 | 2025-09-29 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8468abf1-f5b4-3ab4-98d5-dce013c6acab | -18.1761 | -53.31048 | 2025-09-29 05:29:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20494e24-af91-3652-9ba2-c5e6288c8b4c | -18.2029 | -53.32298 | 2025-09-29 05:29:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f947242-5f45-362a-b940-6cc4eab3836a | -18.21001 | -53.30904 | 2025-09-29 05:29:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e62444e9-b452-3888-84d4-2738d585e3a0 | -18.2107 | -53.30258 | 2025-09-29 05:29:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 57a26890-0a01-39e8-8848-2f03d25c4132 | -18.21592 | -53.30644 | 2025-09-29 05:29:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 79c44e6a-0f75-3de4-b567-a680a4e4173c | -0.99609 | -47.05289 | 2025-09-29 05:36:00 | AQUA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7feec3fc-58a6-3a45-b005-0657ed86fae3 | -2.81093 | -41.7976 | 2025-09-29 05:36:00 | AQUA_M-M | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 482f6a1d-3ac1-30a4-a2c7-f2ccd0d204a4 | -2.87575 | -40.02229 | 2025-09-29 05:36:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d2c3de2d-632c-3fb3-9de8-a22a415d7964 | -8.29826 | -45.47102 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4c79fce6-672d-3db6-826b-aa3c51be56ee | -7.22804 | -44.77414 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| f2248cf2-9c44-3cf5-b46a-fe7684d63708 | -8.15184 | -46.39439 | 2025-09-29 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 39e3a748-e687-3074-995e-23efc2236df9 | -8.77062 | -44.94455 | 2025-09-29 05:38:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4bee60d0-851a-33d2-a922-f7a85046c39d | -8.25362 | -45.48912 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5127e036-7e8e-3493-8b00-1e37e9ecca1d | -7.89038 | -44.59877 | 2025-09-29 05:38:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7aadc90a-a57a-35f2-aedf-49d4bdf3dd71 | -9.79585 | -46.94493 | 2025-09-29 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ea43e48d-55eb-32b1-8337-38aafcfc4e08 | -5.03784 | -43.60664 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ceb5b771-1d83-3b15-940c-ed0b2f29b1c9 | -6.56822 | -43.39869 | 2025-09-29 05:38:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 11.5 |
| cdc6c1c7-dfb3-320b-b307-e3dc8839474b | -7.21845 | -44.76587 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f7b0cf80-c3bb-3c6e-a607-8de219e33f89 | -6.27422 | -42.48353 | 2025-09-29 05:38:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| af25f767-034e-34aa-8cbd-6f60ad202753 | -7.22832 | -44.76736 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4ae736cc-9086-3e2c-ac1b-5b9e1633fb13 | -9.04974 | -46.71127 | 2025-09-29 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 80c93d80-7e41-38cc-bab7-8f81be6d51cd | -8.30095 | -45.52027 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e08070a0-1fb1-3bd5-8918-1a44d484c2ba | -5.18933 | -43.75848 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e46baa0a-18b3-365f-9242-320a036f0ea6 | -8.86808 | -46.60463 | 2025-09-29 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 54ec1c5d-f290-306a-b9af-ee470a73d627 | -9.79824 | -46.93034 | 2025-09-29 05:38:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b5c4ec34-5fa6-37db-8558-b4f17a965b2a | -4.7047 | -41.98819 | 2025-09-29 05:38:00 | AQUA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ae2af2a1-f544-3fc4-bc50-7d34e56ffcbf | -8.82003 | -46.19469 | 2025-09-29 05:38:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7ea46b2a-afea-32ac-94a2-328f325a0fd7 | -7.22485 | -44.78983 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c18c9710-f3cb-37b1-8230-27cb352338b9 | -3.09211 | -47.02021 | 2025-09-29 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e2c8551b-b5d8-3b50-a8be-2492c101a83b | -6.8977 | -44.52692 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 054c0509-b230-3280-b800-065fa955f6f4 | -8.14084 | -46.39308 | 2025-09-29 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b04023e9-fbef-3808-a971-7f28f067a043 | -8.30286 | -45.50811 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c624fe10-a554-3dbd-bbe1-989267a620c3 | -5.46055 | -41.07513 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| da30dcee-daa1-3c60-bbab-a38f77e9a6bd | -6.90886 | -44.00128 | 2025-09-29 05:38:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5365c4b-36bc-3edc-85f3-08b3a442ecfc | -5.73561 | -42.86086 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3cad86bf-2b62-38d4-809c-d761a00cabea | -8.0485 | -47.17318 | 2025-09-29 05:38:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fc3c2ef5-6758-33e5-ad94-22e7078c735c | -8.13858 | -46.40717 | 2025-09-29 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fe2700c0-5273-39ac-951f-e40e458fcc91 | -2.57659 | -48.41083 | 2025-09-29 05:38:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 40297d68-2ce9-3a2d-ae84-e159582d3004 | -8.86579 | -46.61894 | 2025-09-29 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0413e61b-5615-3e42-9e2a-c1da3e38d5c0 | -6.10555 | -41.82096 | 2025-09-29 05:38:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0d3dc7bf-d2c5-3a7a-84f7-c7b82c0acec1 | -4.70607 | -41.97925 | 2025-09-29 05:38:00 | AQUA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 529c6639-b139-347b-929c-23f0d2fb466a | -2.58072 | -48.38546 | 2025-09-29 05:38:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| b44730f5-9212-34bd-84c5-551b29f72a0e | -8.30476 | -45.49603 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d75be5e7-9b74-3ae9-a2b0-0a8229261cfd | -9.27393 | -45.73308 | 2025-09-29 05:38:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6a8a75fe-3c88-32c4-b4a3-5f05b9161cc4 | -6.06305 | -42.47675 | 2025-09-29 05:38:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c1b51591-ee8c-3830-8345-31dff7a976db | -6.06152 | -42.60686 | 2025-09-29 05:38:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 49b79768-76a1-3d1d-9593-1f192479e1ec | -7.892 | -44.58836 | 2025-09-29 05:38:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ca7bb7d8-88bc-361f-9422-a1ed9ec0a894 | -3.0904 | -47.01471 | 2025-09-29 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 159fadbc-52d9-3587-9770-af7080b14d5b | -6.14171 | -42.80409 | 2025-09-29 05:38:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README79.md)
