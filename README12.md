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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b01a2b40-6d77-3389-8a66-986090e631f5 | -7.45894 | -46.14628 | 2026-09-04 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a08036d-f49e-31bb-8576-1d422340c6f2 | -10.64304 | -50.38933 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 65b9aa08-2f9f-3a3e-8e15-661860e2fc95 | -10.49743 | -51.32521 | 2026-09-04 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49c6ea1d-6bfb-3f54-b6cd-7638058fce94 | -10.57733 | -50.03027 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d003dc64-ad01-3165-bb3d-11d3492871f5 | -7.45814 | -46.15106 | 2026-09-04 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d30c8848-d118-3d7a-bb57-03d953998e53 | -10.84096 | -51.78666 | 2026-09-04 04:19:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b8f313a-110b-3451-a81c-045295bdeeba | -6.42477 | -41.53938 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd0e2114-ab06-34e6-a450-79fd81c544c0 | -6.11541 | -44.68274 | 2026-09-04 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a07d55a-021b-3b97-82b3-9ecb9dd58ffe | -8.11623 | -54.78787 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c9ae0e13-af37-3e26-b0de-8109f28cc354 | -9.58065 | -40.34242 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| ae690c9d-e373-3cf7-ac8c-ee3b42641f9b | -6.11178 | -44.68215 | 2026-09-04 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 515dd90b-ae22-3df3-8913-e7f4587b3067 | -6.77145 | -41.17032 | 2026-09-04 04:19:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a91e5c26-7820-36f6-8eae-b68c0a0b57e3 | -11.51466 | -46.8988 | 2026-09-04 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2926da2-a7a3-3b46-929a-e4ddc91f06d8 | -4.99346 | -50.43697 | 2026-09-04 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8ee4d3b-c89f-39c1-aa40-e30cf5006da5 | -10.63835 | -50.39799 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a0982fa-1f56-36dd-8d31-817f74c5de8a | -6.09686 | -44.14647 | 2026-09-04 04:19:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d18dbaa-6cd8-3098-8990-b509e6dd6969 | -8.5021 | -54.64208 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 47b0657e-1747-3279-9ef8-85917d11f825 | -10.65171 | -50.39656 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3dca7fa2-2ce7-344e-92e1-052132d5754b | -11.27629 | -45.72151 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8281d276-79a5-31b9-8500-b77e191db06d | -10.26223 | -50.03424 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f3c7ea51-fdf5-35c9-bfb1-b102ac4f48ef | -8.48784 | -54.64524 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 245a15be-ca34-38bb-80b2-8ccc1874a669 | -10.65554 | -50.40286 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a31a63bf-01c3-370e-b64c-2c75b6c68ad3 | -5.71848 | -44.38883 | 2026-09-04 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9a66e1d-5098-3b16-b1e6-6744a093453f | -10.90757 | -45.35912 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0334e676-8985-320a-b19c-00650f8161ea | -5.54452 | -45.20094 | 2026-09-04 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df174a97-cf16-3fb6-b85c-4254f7c9a5f7 | -8.1146 | -54.77653 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c69e39da-107a-36c5-a6fa-2f35dd43fe50 | -10.49461 | -51.34012 | 2026-09-04 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efed9afa-c237-3496-9144-13d10fa64675 | -11.52226 | -49.20488 | 2026-09-04 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d317d9df-7ef4-3f4e-8635-89601e7bccc8 | -13.09674 | -44.49847 | 2026-09-04 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c013def5-a9bb-3712-9b5a-92c231194348 | -9.01257 | -40.99636 | 2026-09-04 04:19:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2fd05312-1260-3417-8dfb-6e7ba71f6ab5 | -8.10562 | -54.78706 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb41fd76-ee30-3839-a94d-9a9cef55a2f2 | -10.90952 | -49.61728 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68fa6db5-c5bf-3147-b5f3-fd4216e4ff3a | -10.64766 | -50.41812 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e3bea6ec-64d8-350d-b6d7-3584d247bcb6 | -4.99404 | -50.43362 | 2026-09-04 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0f00b84-111d-32eb-96c5-ccbcf250fa45 | -8.10398 | -54.77943 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| af21fde6-a26d-3699-b2ef-d317ad3b920c | -8.10846 | -54.79236 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2aab3ad0-ce1c-3f2e-b49e-0a70fadf86f7 | -8.49884 | -54.65893 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d52ef9d-b8f9-385f-88d3-c18fec6dd5f0 | -8.31509 | -37.26891 | 2026-09-04 04:19:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 03388c6c-7e84-355e-ae4b-d9b914d32a3a | -5.7991 | -43.64602 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69ffac4e-fc2b-3f29-84f7-636b2f8df2f6 | -8.10676 | -54.78122 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2742e41a-caf8-3668-a526-898a602e25af | -11.27125 | -45.72936 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9626da96-4746-3e98-a11d-6559811adb5e | -8.10408 | -42.59694 | 2026-09-04 04:19:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14f78dcc-5326-3e1e-9419-1659965f19af | -6.31412 | -46.09105 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78e81991-e955-3530-a289-1241f890f4ab | -6.11589 | -44.681 | 2026-09-04 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4e9434c-c0ac-3de2-9a09-71174f0f4266 | -5.55449 | -44.23419 | 2026-09-04 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a08c9e05-9afb-3d0a-b4e7-49962e872843 | -8.4414 | -54.68828 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09974360-74f8-3ae3-98c4-20ec96810897 | -6.11658 | -44.67684 | 2026-09-04 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 460feb50-d409-32f3-912e-bf700377b06c | -5.79848 | -43.64983 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cb87618-7146-3495-9d20-80d6af4a0141 | -10.63546 | -50.38626 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd125b0d-adb0-3770-9050-f94e776afac3 | -10.65481 | -50.39 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| d6763c27-8854-3004-bb69-ddffedf9e2e4 | -10.64788 | -50.39025 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 047c3fa2-0949-39fb-b948-7216c97eb052 | -10.91181 | -45.35563 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4119bc64-4e20-3331-807e-1d627f3363eb | -13.40302 | -41.88785 | 2026-09-04 04:19:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3a8f8112-f353-3ab5-b2e6-56d7153b5d74 | -8.44027 | -54.69424 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aaf1a800-164a-3380-8084-c24bc80fb752 | -6.33062 | -43.8189 | 2026-09-04 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 846f025a-14b1-3f81-92e6-aab28c2841b7 | -5.80219 | -43.62702 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f8d7883-698b-32da-bed7-08d20cacf542 | -7.59738 | -44.74892 | 2026-09-04 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3cdcbc48-e86f-33a5-bbd4-e65e620271e9 | -10.65675 | -50.40712 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 456e76f5-50b2-3d3f-9552-5516e2340763 | -11.26837 | -45.72461 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec0be525-d433-3d35-bfe9-3f70398c340e | -10.65384 | -50.3954 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| c83c1f33-725a-33b8-8bcb-9a2a521b20bf | -10.65352 | -50.41364 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4917fe4-ab59-3105-bf25-657bc6da52c2 | -5.55115 | -43.43265 | 2026-09-04 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43efc2ac-a23f-3007-9806-99bc2cfca419 | -8.48566 | -54.65644 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77f94109-1c8e-3f20-b9ab-0964522d50ec | -11.0419 | -44.34394 | 2026-09-04 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64079cd0-3c9b-3f65-bb1f-9684ae760a26 | -6.3152 | -46.08959 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3a2e55a-1142-3e16-8443-042be8a4b946 | -11.27703 | -45.73886 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40cda1d7-1352-3ddb-97eb-4d8a90bff8c9 | -7.59447 | -44.7443 | 2026-09-04 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3de003c2-0189-36ca-99bc-b9460006b391 | -13.39964 | -41.88734 | 2026-09-04 04:19:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66efd7fc-92af-3126-ab2e-c99bb2e4b371 | -10.65373 | -50.38578 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1a83fca7-83ca-3143-b6e3-3ddb89993167 | -8.49225 | -54.6577 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dde5a9a4-c083-321d-b404-ea3eb268a2ad | -9.57605 | -40.34943 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 09276f6f-9088-39b0-b318-1ca56bd0bff0 | -8.50651 | -54.65459 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fd6fb12f-a48a-380b-add0-5454035a4fe7 | -8.11065 | -54.78073 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02056021-b35a-373d-99d9-ad5059a26cff | -10.65272 | -50.39117 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e62f761d-2060-335f-baff-bb075321163f | -10.64203 | -50.39472 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a8aaa822-3cb9-3cc8-8436-d5b305c833f1 | -10.64889 | -50.38486 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9148a562-a064-3646-a687-49ba7baa93a6 | -10.2677 | -50.03189 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 93f6076b-c55b-3638-96ef-b758e967d53c | -11.28279 | -45.74847 | 2026-09-04 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 179c1211-43e7-3cc2-aba6-1733c5d40bbc | -9.58122 | -40.33865 | 2026-09-04 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 7efd3021-ea35-32f1-8b10-8e0b4733dd80 | -5.3241 | -44.84299 | 2026-09-04 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3080bc5-bbc2-3527-8945-21439023c01c | -10.66038 | -50.40379 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e06f9fb-9678-39e0-a786-8a4bef84f6ae | -9.01202 | -40.99995 | 2026-09-04 04:19:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 81ce9b3a-5042-3d1c-89af-d748f8818f89 | -6.77478 | -41.17084 | 2026-09-04 04:19:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d39a7541-c566-3cdb-b1eb-5b36868829a8 | -10.65095 | -50.38365 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| be8b53fa-1094-3b65-b14d-a4b7a9df0eb5 | -13.40358 | -41.8842 | 2026-09-04 04:19:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d8750324-6fd3-391c-96a4-7d88092f4248 | -10.6382 | -50.38841 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cbe3e47c-c1ed-3a1b-b918-417a2b939cd3 | -8.11732 | -54.78205 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 719c4863-7195-3647-8473-e7377bf54864 | -8.49445 | -54.64635 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97f1d8d5-5e57-307c-997e-939d5eba7dcc | -10.6403 | -50.3872 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c15acd6-6b8a-37dc-a3bb-1ed96498ecfd | -7.59806 | -44.74479 | 2026-09-04 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4700ec7b-de51-30a1-a073-c4fcff70e27e | -8.49551 | -54.64089 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79c55816-df79-35ec-b896-44e139d0154f | -10.62867 | -50.39611 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7e4344f-09e3-3ed6-b6aa-5e28df633c65 | -10.48184 | -39.64886 | 2026-09-04 04:19:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ea74f0a0-eb98-387a-a9d5-1897909f380b | -8.12011 | -54.78378 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fb8ed0b8-ea32-3434-9d41-4b404a200e2d | -7.61365 | -44.7392 | 2026-09-04 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1741036-01a1-3bcc-acc9-84903c4bd0e8 | -8.10955 | -54.78658 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 89e54548-59ff-34a0-8b5f-44c03ed3e58f | -10.64609 | -50.41066 | 2026-09-04 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7cec0979-72a7-3adb-95ec-7f6259d6dc39 | -10.3151 | -50.34165 | 2026-09-04 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94e315e2-0df5-3af1-9198-e0ae02edfcd8 | -8.49334 | -54.65209 | 2026-09-04 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f659edc8-75fe-37b0-b22f-61213c4cf6e9 | -10.49525 | -51.33672 | 2026-09-04 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README13.md)
