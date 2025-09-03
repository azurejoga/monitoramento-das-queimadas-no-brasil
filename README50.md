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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3da78dcc-9c83-3de8-9f38-da143a56cef7 | -9.69594 | -51.04293 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2418305a-9926-33b4-becc-e7cbf66c56d9 | -11.60277 | -52.08009 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd55cb58-be62-35b6-bcd1-fc6a1acf1152 | -11.38077 | -43.56828 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38f38ac1-0258-3f42-883b-49473b50e4c7 | -9.1368 | -49.64383 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec031e77-15cd-3c01-83b1-726e4fa640e0 | -8.37279 | -48.30837 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a95c3f2e-9bb6-3e85-bcbf-114edf198451 | -6.54812 | -44.5673 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4d74032-90a5-3dad-ae3c-1a2b14a25a6e | -11.63521 | -52.04573 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e213c3c8-4871-3987-813f-6f78456b3158 | -8.05681 | -52.34692 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc2db730-67cb-381f-8b97-0227d2234cac | -6.199 | -43.34507 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c40c81b-2a85-381c-a217-9531744d91ec | -6.35122 | -45.6628 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fbee1a7-5762-3d74-ae3b-7269de902879 | -9.25574 | -56.8993 | 2025-09-03 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e812034a-e86b-3779-b92e-0dec901d0b06 | -8.86252 | -52.02934 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fcdec13-407d-3a35-8069-314799e2bf52 | -8.10064 | -49.93835 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9c48e8ba-e30c-3256-9058-9953184483db | -7.5586 | -45.71041 | 2025-09-03 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9de879d6-21f8-31a3-9b09-9b08eb77b2e5 | -6.81865 | -52.81576 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecd3c3e0-409f-3610-9a20-51a1b0459365 | -8.06864 | -45.37817 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c464a4a0-b94b-302c-96d1-4a49617ccebd | -7.94529 | -45.90961 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a947e4ff-c2b4-3cf1-a3c2-94fd6cd888b9 | -10.98669 | -46.82977 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11f5e5e6-3bed-3828-b3fc-53105d2a1db1 | -10.97162 | -50.91915 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43b35149-06ee-35c4-b033-b157961a5508 | -9.99722 | -46.89081 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dd55e57-d44e-39df-a758-6c6d4e81846c | -6.79166 | -52.81148 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34c396ac-e069-3ac5-8e58-31adceec29d2 | -11.12105 | -44.65213 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43fa6082-73df-3d69-90ad-5ee2357ec67c | -6.22885 | -43.40509 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d256ade8-c391-32ed-b65f-a1805dcab573 | -11.27481 | -48.94715 | 2025-09-03 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4271f410-1272-303b-a35f-626c22061662 | -9.7713 | -50.01572 | 2025-09-03 04:46:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49d4d807-bb66-33fa-acaa-fce50fea0467 | -6.97687 | -43.28746 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 446b4a44-7d9a-3b93-abb3-2f43ad2e9b8d | -6.46842 | -53.40109 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7afffb7-9c50-3a1d-aa16-037a6e8f80df | -11.63579 | -52.06381 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9931ddf-c3eb-3af1-87ff-7a62c1566fa9 | -7.7029 | -48.74927 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| be01805b-ea20-339b-ab0c-e9d7cda67e19 | -12.57652 | -44.78526 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f029f9d-db8d-344f-a188-98813593ef43 | -11.05617 | -45.40115 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a65010e5-a88a-3b4b-af77-5a0beee7c675 | -10.25354 | -48.25793 | 2025-09-03 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fcdd4535-7f33-372b-aabc-dbd5f2a4e391 | -6.43594 | -58.13956 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af40358f-84da-3841-946f-15c030ca4edd | -5.8084 | -43.22828 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa4bfe6a-8d4c-38b3-9620-fe5daed21bcd | -9.42763 | -48.35684 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88b5b930-4f52-33d0-8ae6-3abb2aefc5c3 | -11.80386 | -51.5485 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0485c6a-2bf3-357a-9a09-e6f94aa96688 | -9.26036 | -56.89645 | 2025-09-03 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15efd20a-1161-3ff0-8c7a-6e2f195f7e7a | -5.70438 | -45.14162 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 153dd3fb-b169-3b6a-a209-8a51e34b9705 | -11.60945 | -52.12428 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62ab6435-d9bf-335b-9e24-ddfec60301b8 | -7.90485 | -46.45583 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8788f142-dd41-3955-af6e-c783a39be788 | -6.73932 | -45.15027 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6026351b-7049-3ece-bdb9-3bb343c36a17 | -7.94142 | -46.55452 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd0246bd-3bed-308b-a31e-333584c8800f | -11.67272 | -52.17798 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e0143a-250c-3945-b67d-0541a3c02594 | -11.61047 | -52.07413 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a47c1f6-b3d3-3b67-89ee-c7c4dabcb255 | -10.05792 | -48.08678 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aee3ec3b-4ae8-30f5-8d25-f6316b4723e7 | -5.70943 | -53.69183 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 634cfc79-9b24-38fb-b345-3e7d44791ae0 | -11.21177 | -55.07734 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67a73491-884b-3e5a-a500-fff60d2ae7f6 | -7.70231 | -48.7532 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 055c9997-a73c-3a66-94ee-a1dc5e1e202a | -10.1304 | -46.24824 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3275d7f-2e16-3435-aecf-ead0f6497fc1 | -6.23298 | -42.42842 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8fe921be-9c1e-381a-8a45-7b6c4b75743b | -7.29097 | -45.28455 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72f1cc5e-4e1d-35b0-adef-339dd5ff7978 | -4.24573 | -55.53598 | 2025-09-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9672e919-3efb-3aa2-b7a5-0fa740988122 | -5.86957 | -51.71869 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8ad2c80-bf86-39db-9084-3a670bcce7de | -8.86967 | -52.02691 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d434f0f3-8f28-34e5-8924-aad2b39a829b | -9.63482 | -47.85692 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7bd65a8-7647-3ecb-b675-0a4bfcf83ec8 | -10.916 | -50.84051 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caf5b9fe-0e51-334a-9f35-de85b08a7b8a | -11.02853 | -51.48378 | 2025-09-03 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64055110-cdda-3568-a6a7-ceb127d5d190 | -6.69615 | -44.18663 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14b1fbe4-add3-3a07-b899-63dc1bb9253a | -10.91319 | -50.83636 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b239c59a-cfda-3303-9110-8becec5084be | -8.09499 | -47.591 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef37c82e-5a75-39a8-8ff2-0077542018a2 | -7.69644 | -48.74425 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ce95e23b-4e6e-3d8c-966e-207fa05efc16 | -6.26268 | -43.30451 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 625a5ac0-c9b6-37c7-96f0-f0d64c489e85 | -6.46936 | -45.41103 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a4c1bb7-e6c2-31c3-a889-2516f3d32783 | -6.85635 | -45.54444 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f92b3c4e-012e-3b13-b14f-da97975b8ab9 | -11.02211 | -46.96145 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1ecaa47-9d84-3d03-8c88-3842f524056f | -11.11971 | -44.66264 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b81622b-adaa-3669-aefb-38ef78be9b7c | -10.45298 | -53.62077 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce53aae9-5549-3eae-8f4e-d76a2930cc41 | -8.55324 | -47.47541 | 2025-09-03 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 194a2360-d024-387b-809f-40f59925d170 | -3.73052 | -58.84588 | 2025-09-03 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6603fe70-9359-3821-8ca1-7951641c81bc | -10.73047 | -49.58958 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 721f5895-4874-3273-a202-8d050f378f8f | -9.69261 | -51.04238 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53503bd8-d41e-38b8-926d-41e67a18ffaa | -10.48493 | -53.63718 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4f77fca-2223-3f7a-a58b-d3dd47eb46cd | -6.2636 | -42.59909 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f83d2cd1-25c6-324c-9680-7a683c8fedbb | -4.58019 | -48.01873 | 2025-09-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95c7e750-e59f-31dc-ab16-23213e1ebe29 | -11.62543 | -52.13043 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a87f7a3-0b1c-35d8-bafb-640bf786a9c6 | -7.90289 | -46.44089 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd8f1cb5-6dc7-3a5a-9a8b-105b67522cec | -11.59514 | -52.12918 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 030b9cb0-64cb-34d5-82c6-7a1a700ca920 | -5.503 | -42.62675 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba2ead56-4434-3473-bb3a-04de6baf5ebe | -6.97838 | -43.27623 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f6b17fde-4e09-3c1b-af8f-e1e30449ff45 | -9.22657 | -47.12751 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfd353c6-6d88-3855-9dc6-758c8c7ff1c1 | -5.87148 | -57.77059 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4fea70e8-cf0d-3cfa-8635-0c9255b9f64e | -8.06569 | -52.35538 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02ffeee8-1cb6-3ce6-b096-29d422f9adbf | -7.47904 | -44.81342 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7df459a5-09f4-33f3-8749-3a8634da3d20 | -7.71627 | -50.25298 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d386f21e-e7e1-34a8-8451-47265b53d915 | -10.45239 | -53.62442 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 175bb7ae-a9bc-3822-814c-9f926f26cffe | -6.45414 | -42.38291 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93f20307-8b41-34d7-b285-9b840e422fa8 | -6.87246 | -43.83781 | 2025-09-03 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a776086-760a-3130-abd0-8b93cc4a651e | -5.35716 | -49.15777 | 2025-09-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b8b7afb-c41d-3cca-a0a8-3e978ae82541 | -11.63027 | -52.05574 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88126cf1-8f43-3ced-81f1-382939ea7d27 | -11.00515 | -46.93302 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b4605e5-58be-34ad-a598-a0d6645ae800 | -7.25757 | -57.54229 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5777a209-44c5-30d1-9b26-34022df07a35 | -5.88346 | -43.01368 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 176f2a41-6426-3808-8100-ebef1cbe17b9 | -7.25257 | -57.54562 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 406725a7-e30a-39ea-9081-564b7592cf0d | -11.67824 | -52.18605 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0c9490f-7e9a-3e82-96db-743860f716cb | -9.14085 | -49.66387 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a41f36ad-f7c4-382e-a2c1-93c713563351 | -10.14253 | -46.25681 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 153b1e23-ed8c-3f15-aab7-ff27a4f3ce80 | -6.37601 | -43.00512 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d35b909d-1e16-368f-99df-800cf8481c1c | -8.89061 | -45.79351 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4ae858a9-86ff-3df5-a215-fb2e9f96b44f | -9.74296 | -49.41184 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 985206b7-9bde-33de-a834-2e3bf68a7a52 | -5.87071 | -57.77509 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |


[Clique aqui para ver as próximas entradas](README51.md)
