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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abe36133-4e6f-3c94-8796-5f6256c1158e | -5.60689 | -48.098 | 2025-09-09 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 100686e7-b321-3456-b163-70febd00463c | -1.3228 | -50.64233 | 2025-09-09 04:32:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 466463db-5a35-38cb-9bd9-2bdde92178cc | -6.00202 | -46.19044 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4338baf8-9479-3483-8983-7ab8f32f81cf | -6.40404 | -44.43379 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f49aa3a-2323-3c6d-ae05-ec14afa52f10 | -5.67155 | -45.4639 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87834cba-fbc4-3014-9b40-a9989b3106ba | -6.33544 | -44.64494 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0646ffbb-f2cf-3b44-a8ab-4cd5f4c9fe19 | -5.37375 | -45.942 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47fafb9a-2658-3ead-859d-a096790fbcf0 | -5.5797 | -45.04589 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 31b8d5df-a128-3fe6-a1a7-7a54006d0fdd | -5.79196 | -45.43419 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d3d4e1-7c94-3cba-aa88-97e7a3d485c0 | -5.79415 | -45.66825 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce386006-7eaa-3696-bf00-ad7b4675e407 | -5.3504 | -44.79152 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16fbb7f3-84bb-3d9f-9317-b7524b513c1b | -5.43059 | -42.80127 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fc0c6e4-86c6-30ea-a007-6ee6637ac508 | -6.08173 | -45.53175 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca116f3a-ff26-3655-be92-40bb6c339873 | -5.36761 | -44.79838 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3338e20a-916c-3a27-8e9f-8d7e28dad2e7 | -5.8755 | -44.88669 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b54e7093-52f1-3e4b-828f-1ae4113b2666 | -5.94238 | -45.77976 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6e8f179-5b8b-3217-9588-015d51ba6ea2 | -5.71304 | -45.41419 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 286547f0-aa78-37d3-aa7d-98d94b33c2d5 | -5.6893 | -45.11094 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbb222ff-a9d2-3ab4-b117-1b77b48ecfac | -6.3061 | -44.79068 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8b7ae76-3e23-3b33-b226-aa1fa9de546a | -5.85904 | -44.17843 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65462542-88fb-3d0d-8ec2-919f3b31f475 | -6.56657 | -43.14761 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66acd2e8-f13f-3069-b6bb-5fd6bd1f3059 | -5.94582 | -45.78031 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f1d3fc8-e8c5-38d1-afbe-60cc8a2ff68b | -6.20509 | -45.02974 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14367c51-9834-3924-9cb6-25d634b02dd3 | -6.61533 | -44.01792 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a79fd85-c698-3f6a-9a77-240a52da43b5 | -6.6782 | -44.55518 | 2025-09-09 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e63994d9-1b3c-3b4f-bb19-f11ff124236a | -5.88098 | -46.08982 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffccc8fc-f70b-3d6d-babd-ec9f46bb643a | -5.22603 | -43.69791 | 2025-09-09 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99e56345-23d3-3c6a-8365-c35b75931989 | -6.83356 | -43.61927 | 2025-09-09 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03031131-69f7-3e63-abd0-dc510d204fba | -6.58566 | -44.00942 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a236e810-c576-3964-a1e5-62a55d1435bb | -5.9418 | -45.78355 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0c2c2d0-f32a-3d35-9050-f3723df0d9fc | -7.25005 | -44.46132 | 2025-09-09 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37c8a1e3-c6b3-3742-878d-702cc8d6eb46 | -2.63132 | -48.06481 | 2025-09-09 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16a082a0-99a5-34ef-8556-eaaf08c4c8a8 | -5.72174 | -45.40366 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a0745ab-6061-3c81-a61b-f069462aa1d9 | -6.18715 | -45.80838 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7abe8e6-df7a-351f-8440-adf35e4cfe15 | -6.19625 | -43.37156 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a72cb78e-455a-389b-a8d6-bfab745c2e38 | -5.41861 | -45.87732 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ac1b522-7653-3392-a3e2-9f72f8dec206 | -6.7089 | -44.29939 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91c88404-91a7-38c5-a298-79fdc02090aa | -5.84247 | -45.60583 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58497d6c-99fd-38c9-882f-65e1fc6bdce9 | -5.96186 | -45.79044 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a785786-6116-3ca7-9e12-bbbd56c18090 | -5.64053 | -43.64789 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c4bdeb6-68e3-3fbe-b0db-0a820d137540 | -5.67866 | -45.39402 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc9c4f83-b028-3d50-af73-59df336b7b11 | -5.53917 | -42.66182 | 2025-09-09 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f3188951-2bc7-35ac-8b6b-7de3d2311d0e | -5.68714 | -43.90354 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 425a9a66-a868-3610-af54-462f9bffd980 | -6.19521 | -45.80182 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5a4a87e-c8f0-3a53-ab63-cdcfdd582ec6 | -5.73857 | -45.41027 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d43a0519-b02c-36b1-a8da-3d0e3d317179 | -5.45515 | -42.80167 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0f712f0-e2da-3d3c-be22-0ebfbfe761c4 | -5.8198 | -43.97963 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8f1e3ed8-fcfe-3b7e-a3fc-e47418df01c2 | -5.94751 | -45.7922 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81276502-546a-37fa-8520-db0b9f92a323 | -6.82066 | -44.90469 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 538a6881-f8b4-31d5-a194-3fccac02511f | -5.82616 | -44.11857 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18f0a5fd-6a6a-33e0-86a3-4db451a5078a | -5.76293 | -46.5233 | 2025-09-09 04:32:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a6cd281-b722-358c-a846-8a10b8e1e46d | -6.34768 | -43.7856 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0af573a3-898f-3f03-8f50-cea5822bc35b | -6.19935 | -42.47216 | 2025-09-09 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d381b620-f00d-309c-b0bc-b936caf1ed70 | -2.93181 | -48.01566 | 2025-09-09 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec4a5f86-76e8-3b04-aaa0-d51a7f1d9151 | -6.18198 | -45.8191 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d223669d-2b1b-3246-9e72-63e5d227acc6 | -7.25071 | -44.45691 | 2025-09-09 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30eef7f5-9ad8-39b9-a426-15868187246d | -2.62799 | -48.06429 | 2025-09-09 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c40cca14-99d8-327a-8684-57fd501d4033 | -6.40744 | -44.48759 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b874ea0-fe29-376d-9533-cbda01283304 | -7.18725 | -44.90368 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52b9f124-3fb0-3967-aa59-be9a313f5629 | -5.45782 | -43.42169 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47d551b2-8438-3f61-abd5-9308a35e1db1 | -5.88178 | -43.97559 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3aff6ca-2688-3b9f-aaa2-d3d620a9b6c9 | -6.43071 | -44.06064 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 698bdf70-d727-36d8-b6ad-40d7cf7eff29 | -5.81872 | -44.1174 | 2025-09-09 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2ad079e2-d82d-391a-9cfb-b78911ba78a8 | -5.68026 | -45.45342 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ab341e8-a075-39ed-a8f2-7e43fe6890d9 | -5.44382 | -48.91778 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4c85c4f-152c-394e-a2ac-2b0cad2c7218 | -6.19123 | -43.59141 | 2025-09-09 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09f32bcd-10f8-3597-9962-4b838ef5c20a | -5.45168 | -42.79752 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0d359317-3673-3157-bef2-e5dabaf42151 | -6.2388 | -44.61462 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2df41cee-4066-3c99-8df9-209ca81be174 | -5.95212 | -45.78513 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75539174-a296-364d-ba5c-344c5647d477 | -6.39792 | -44.42958 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80e95805-fe4e-3bab-9ae5-0bc7a03dac1b | -5.52083 | -42.67377 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb74bd84-7fbc-3272-85c1-b1c53d6eaa80 | -5.36716 | -44.77748 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc1ce9ac-cdda-3ab1-b099-4eb566b0e6c5 | -6.43582 | -44.05225 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdb832b4-c145-350a-a703-7d9055a5401b | -6.39097 | -44.45059 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98a46225-6245-3470-8531-2700d15f3b77 | -6.44156 | -45.30855 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bcf8eb3-d73f-36ff-b1a8-0f64c06a43a3 | -5.68782 | -43.89902 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6da14590-138a-37ab-9580-6405a50b479c | -7.29614 | -43.69849 | 2025-09-09 04:32:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4c24cf4-64a2-3ad8-8560-8e8cc8b05a00 | -5.45594 | -42.80841 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 26a0d952-3eb2-3edc-a667-e4ea3be85f55 | -6.06723 | -43.12836 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 867fcb96-7a06-3b6b-a4ae-b903c7876bd2 | -6.81919 | -44.96374 | 2025-09-09 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e12ae563-aed2-3349-9870-720f4d64afa4 | -6.19981 | -45.81397 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 751a5bb3-47a3-3a16-b6c4-e915752012fe | -2.51607 | -51.9047 | 2025-09-09 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8c2ea04-9986-343d-9c15-c92eceee0d38 | -5.44928 | -45.28527 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ab4a930-1dc2-3e38-b063-ea4ce3a41fb0 | -6.48632 | -41.76259 | 2025-09-09 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d0c07b31-1cda-3855-93a3-423443d07646 | -6.92442 | -45.51767 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c288283-2246-397e-9b19-273a7be822c6 | -2.92341 | -47.80798 | 2025-09-09 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 862f6521-9de1-3136-9e8c-92e89e81fd69 | -6.30588 | -44.21972 | 2025-09-09 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a18468a-8342-3401-85bf-9204f09bf69b | -5.64124 | -43.64322 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cd18ec1-3add-3281-b78b-c0500871f727 | -5.68474 | -43.89389 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4dc9a44-9e44-3c2c-9f01-f5a397ee9e45 | -5.54024 | -42.65459 | 2025-09-09 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| db3f0fe9-051f-3b83-9481-a2968f07ca45 | -4.97252 | -48.94824 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b69c651-5f13-38e4-a0f4-98d9ec1e71c2 | -6.37511 | -42.57705 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 037bb8d2-21d3-3153-89ba-5b4395faa032 | -6.03541 | -44.42426 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5476c3b4-9d51-3a12-bba2-8f62b6d5ce99 | -5.43198 | -47.32574 | 2025-09-09 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cdc38d6-3f1e-32ce-8530-91bc870573de | -6.3999 | -42.97673 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5d5ad2b-6ad0-3087-81b8-3b41c7d577bd | -4.40734 | -48.94732 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 978ea11f-3b04-31b8-aa5e-69801bb1487d | -5.73567 | -45.40585 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 941cca4c-79d5-3fd9-b7e3-0b3e2d5cee5c | -5.84066 | -44.09772 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1905756-12d4-362b-a488-29a035bf518a | -6.63062 | -45.10863 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 608f0ba8-537c-30a7-bffd-568135f760af | -2.43864 | -47.1898 | 2025-09-09 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README29.md)
