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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06d9786a-0efd-3bcd-a690-16f42cac14b2 | -5.87147 | -46.10884 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebe69c99-8098-38c5-a697-21a464e0806b | -5.65198 | -51.26828 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 474ca01a-4952-335c-9573-a34f21ff7fd7 | -6.90771 | -43.81763 | 2025-09-05 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b66de64-7655-3a61-97ee-d0b300236d3d | -6.20675 | -43.57552 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e9b2714-2586-3dcf-9df7-ccadd2408825 | -5.37401 | -45.10505 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bdd006e-b036-3c72-bca4-9ac1a79fb4ed | -6.2626 | -42.64773 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47bbc1e1-8302-389e-8090-0d17e2ac859f | -6.87874 | -45.57863 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85905822-ab9b-3688-8356-dd03858036d9 | -5.10648 | -56.14144 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e958f336-81a4-39da-a2c2-d4390c65d078 | -6.06513 | -43.33908 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2d90c9f9-9d5e-3e54-8af0-844e8fbcfbd3 | -6.15682 | -43.18182 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5c92c5dc-0e3d-3b75-b4cd-e3ebd53820c9 | -3.49184 | -49.0406 | 2025-09-05 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31198c86-8954-3083-8f92-64466e476a97 | -3.49125 | -49.04432 | 2025-09-05 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6b79bc2-2681-364d-b115-f1b16efd4a84 | -5.75064 | -45.53378 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cf41239-7a6a-3b00-be09-a4c7bfb182dc | -5.87197 | -46.03809 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a19e0bda-7f0f-3992-827c-a162723e7953 | -7.88917 | -45.30596 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 768fa263-7f9d-3399-932b-28c90cadced1 | -3.48232 | -43.33235 | 2025-09-05 04:34:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a43636cf-2304-37e1-a157-180a84e49b4d | -5.44459 | -42.89813 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dd0b4b9a-53e7-35dc-a259-d21ea346b638 | -2.38245 | -47.62658 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b81ffda-ab03-348d-845e-5e865b3b0f38 | -6.01611 | -43.36969 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e7ecdb53-ef65-3ccd-8018-d317a22084d1 | -5.8573 | -46.11037 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb7f2a6-3b73-30b0-af34-329953c5c590 | -5.71406 | -43.10142 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40d6bc22-3b85-348d-86bd-f15427de8110 | -5.10807 | -56.13214 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80b64db9-a18d-35f4-ac7e-2097cd599e45 | -6.88283 | -45.57524 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec9e71bd-5de4-3140-96af-5707aa316c92 | -5.59439 | -51.9457 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be9cf82d-521f-302f-abd0-e5fb2084ee78 | -6.80943 | -45.65812 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 66e06833-4f33-311b-bd20-692f2ebeb9e1 | -4.1578 | -41.66499 | 2025-09-05 04:34:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43252f51-6916-3ccf-b9e7-2b147525d6ef | -2.50951 | -51.82297 | 2025-09-05 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32b8253b-505b-3041-97b2-1e860a3034cc | -6.6877 | -44.79982 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa1f19a4-c621-32d2-b187-6a083951dd37 | -6.21098 | -43.40252 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b18adb94-01f6-3f66-924a-ed408f809989 | -6.19811 | -44.33628 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45fa383f-0594-3835-b876-d04552f40022 | -5.70135 | -45.40607 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e500281a-d2ae-32c9-8778-9afba056d51a | -7.89274 | -45.3065 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eabfb5d-fecc-344e-86cd-3504433cf26f | -5.89757 | -44.16546 | 2025-09-05 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fa7cd06-45e3-39a6-a2fb-23c731bad26f | -4.27373 | -48.18514 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 275d8a9f-4b53-324c-a174-f3033e467ff0 | -6.4964 | -43.73408 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67f32f89-3cfd-3ce9-be21-d60793654857 | -4.46118 | -41.00976 | 2025-09-05 04:34:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 35e6c086-8dd3-340b-91f9-d140b8e283b7 | -4.17349 | -42.02413 | 2025-09-05 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6a077fe8-7251-3c47-b84e-e6abf76c3111 | -6.20785 | -43.39697 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af5df8e1-9f2f-3aa8-9ca8-e57dfe395cc4 | -6.42074 | -44.68782 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57eb26b3-f0c2-3476-8da6-c3b6ba614573 | -6.3182 | -44.43233 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42238ac9-b372-3b29-b941-64cd667be9d8 | -5.45397 | -42.81936 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ad8b46ad-7edd-324d-adcd-293b5e22d68e | -5.75237 | -47.34335 | 2025-09-05 04:34:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 565839c1-4b31-3c0a-8a7b-046ee88742f3 | -3.68274 | -49.02469 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 261fdfa1-69e2-3a94-96ab-b0e3098aef87 | -7.21253 | -44.18989 | 2025-09-05 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bdaf3ec-9871-3b62-9e93-0e16973251f2 | -5.39346 | -45.94711 | 2025-09-05 04:34:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 864a682b-01ef-3025-9712-4ead4238b6a6 | -6.26508 | -53.44301 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59efad8b-f115-3fbe-b449-476fae738cf3 | -6.37989 | -43.81409 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e05f8715-4797-3e4d-8aeb-3cf7c07b702f | -5.44281 | -42.8124 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 32132404-cbff-3117-ac5b-92a1cbcb2283 | -5.79525 | -45.6242 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 926e9701-0ed8-3195-ac8c-ef6ef31246d4 | -6.22005 | -43.53845 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1baf638d-da3f-3d6b-b579-87ec35af20a2 | -5.09457 | -56.14884 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f685db53-6e2a-3775-9b4a-5214c4a63ed9 | -6.20472 | -43.57287 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34c1e194-ac3b-3c93-9251-c7aeeca47977 | -6.17217 | -47.28399 | 2025-09-05 04:34:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1414000-dc87-3eb2-a43f-6e4afeaf234d | -6.67119 | -48.3939 | 2025-09-05 04:34:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 703410f9-7591-3a6b-b24b-a7ee8effc4d8 | -7.06702 | -46.19721 | 2025-09-05 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 554708ee-1042-3911-a983-3b56049b3ba0 | -2.8964 | -51.47854 | 2025-09-05 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1575865a-7a0a-3dc9-a084-629919b7d205 | -7.89334 | -45.30242 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f792c8f9-ce5d-3948-96a7-45ad0e9c1395 | -6.15732 | -43.17273 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 483e20c6-d2a4-3729-be60-b7a59f1994d4 | -6.37916 | -43.53509 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b69b0a0-185d-3030-ad17-73e3963f5630 | -5.98889 | -42.98988 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 62d8befe-0409-3fc7-9e26-2d4a4e153def | -5.42715 | -42.86182 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 09806b95-e629-382b-a91f-0df09debeac6 | -6.26041 | -43.50534 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4bbbd76-0047-3749-8bfd-b4b905bb76ee | -6.59322 | -44.56158 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 47077e13-9adc-36b7-bfbb-b93ba91c1a7b | -6.24995 | -43.28003 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| df4db56a-6e18-3a49-8a6f-081e25febf13 | -7.95326 | -44.94799 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00686abc-e4fb-3972-9f04-ea74d5d70bee | -3.99557 | -47.37163 | 2025-09-05 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9ebb3c8-4744-34f6-9cc5-96362dbb42a5 | -6.05298 | -45.99398 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b76f752-6517-3613-aea0-e1759c9cc6b5 | -6.00515 | -46.68379 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d902d8-5377-3821-80b6-3789d012ac1c | -7.70308 | -45.17652 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2953dc93-f51f-3657-b352-d02bac16a5ef | -7.69889 | -45.18007 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5070fc2d-08b1-3abc-932a-20b1fc23cf6e | -2.34403 | -47.58841 | 2025-09-05 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f4434e0-bc91-33fb-a4d9-d7505625ffa7 | -4.17653 | -42.03207 | 2025-09-05 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 27e54fd8-a2b9-33df-8d52-8fec66cd66e3 | -5.70815 | -45.15445 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3457abb-1591-31f7-aafb-294cf2ffcb78 | -7.60989 | -43.84383 | 2025-09-05 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9798a36d-b888-3343-95e8-9e4e6ddbb7e3 | -6.21656 | -43.56216 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c45f4084-3cf6-35a0-b16d-267b046b4e03 | -5.81977 | -47.77678 | 2025-09-05 04:34:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b5d840b-700e-37b3-b0d7-96f04cc48dee | -3.32743 | -54.90753 | 2025-09-05 04:34:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 265c60f6-bdc1-360b-bdfa-92b0985370e1 | -5.42638 | -42.8669 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4f554f26-ee05-39f5-8cb2-0d9292950101 | -4.15298 | -41.6684 | 2025-09-05 04:34:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3b2b164-1867-3b86-a1ba-b5b372fe6d05 | -6.26996 | -53.43988 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1915247b-d382-34e9-9f38-6d9091e7eb45 | -4.79183 | -43.81885 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9540735-0481-3822-acde-b5e17dc50494 | -7.16386 | -43.89398 | 2025-09-05 04:34:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd491247-9f8c-34bb-abc3-068428e4a3ca | -5.79928 | -45.62098 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f69646ac-5d5f-3666-9fb9-a5521579b2b8 | -6.66951 | -48.40444 | 2025-09-05 04:34:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d39bb0e9-e68a-3e4a-b14b-790bb49fc943 | -6.59272 | -44.31912 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfd8ae48-7b20-3cc1-98fa-b11ea11ad5a5 | -6.54302 | -42.94119 | 2025-09-05 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec799f7b-fab6-3f18-9e54-df15df9e252f | -7.35285 | -44.3281 | 2025-09-05 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 933d9b9a-9581-3dad-8ff8-feaddbcb12ce | -6.11995 | -44.11269 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 455efb01-7de1-3b02-bc12-8619f26af81d | -6.54991 | -43.72955 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b138275-a57b-3a3c-af81-9ee09b67d2cf | -6.2293 | -45.1653 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d611423a-4aae-32d5-be24-1a339f7cf417 | -4.06959 | -48.04148 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c4df579-0e63-38f6-9674-969318e826c3 | -5.44853 | -42.81555 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cd906129-02a2-3274-893b-a2358ec161e2 | -7.95627 | -44.95272 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52d6a35c-9532-39c6-88a1-0884fad7afb4 | -6.1214 | -44.11474 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17d57331-3979-30f1-bae8-985e71e095a1 | -6.25801 | -42.65065 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9791b7b9-62e2-3a5d-aa9b-5394cceb0587 | -6.21152 | -43.55414 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b584e4b-9629-3f24-adff-1a59f1cead68 | -6.22555 | -42.62177 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8394c71d-b2ce-36d8-831e-83dce9de70c8 | -2.78586 | -49.62239 | 2025-09-05 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b59a242-8f0e-396a-881b-7e62ab7490e9 | -5.34214 | -42.7953 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7945d1f9-554b-3581-bf1b-9fffca200cd8 | -7.89364 | -45.23667 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README18.md)
