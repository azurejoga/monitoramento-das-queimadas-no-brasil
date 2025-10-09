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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6948376-5b64-307b-b970-244a2d1378eb | -7.69668 | -42.38617 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05467878-4dbe-3549-b811-2c3b817cdc94 | -13.6748 | -48.75086 | 2025-10-09 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d9b170e-6e20-38b7-bc0c-2423be494d05 | -11.13897 | -47.74771 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3ff4d6c-533d-3254-9c77-d9bfec2d8966 | -11.85154 | -45.07075 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ae308e9-fdc2-3ba4-a706-2f1a2fdc3e79 | -8.19603 | -43.35881 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a7682cd-50aa-3dc9-b60c-bf7e08c804cb | -7.20325 | -45.49109 | 2025-10-09 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77847d79-723a-304b-bc79-dd3d1648d418 | -11.79867 | -45.04138 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52faf17b-a87e-3371-a648-9e4f8675b82e | -13.80107 | -45.84908 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 487a7073-b583-3aee-83ea-8d48c7494a00 | -9.1706 | -47.81493 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4de4b752-df9c-3fc8-8d0b-214952c988af | -9.18266 | -47.85213 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d16172a-1d13-31e7-89cf-ee450da161bb | -13.77513 | -45.84122 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27dfe92a-4998-3544-a9fc-087ebb2404bd | -11.88217 | -45.50621 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa4bf041-d121-3d0f-8f76-b08dc6f03bbc | -7.15469 | -46.88193 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e0f9c8-5cd5-31ad-918b-319dca9a1de6 | -7.76495 | -44.04094 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 12f2c407-1c29-348c-b28e-2234c4ba51e6 | -8.55339 | -44.62356 | 2025-10-09 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf298f37-d371-38fd-b9cd-6fa06bf184df | -14.51208 | -46.63906 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4259d61b-f1ce-3557-a662-855ea97cfa97 | -13.81323 | -45.8365 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c38f659-a884-37da-8a6d-ec66951ad7ac | -8.15374 | -43.33406 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 05d66837-dc67-3475-912c-ad93c7488b72 | -10.4421 | -46.63609 | 2025-10-09 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e2d7f7e-3dcb-3464-b966-92379e2c25dd | -7.99707 | -44.46751 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d4234cf-73f8-3cba-9cc8-fa765207b6ba | -12.06651 | -45.73787 | 2025-10-09 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a430e1d2-5c77-3c2f-ab15-856215f31745 | -10.73646 | -49.33681 | 2025-10-09 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a542095f-e5f7-35f5-b15a-7de059111e7c | -11.79242 | -45.14477 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c5fd3fb-4017-324f-8e27-f8b6bf48487a | -11.76498 | -45.14837 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6da97fe3-7c5f-3ad0-a3eb-60e51c5f0537 | -12.42081 | -45.68687 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e52d101-2d4a-3d1b-b909-9bd6e59a7d6a | -11.78434 | -45.15508 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ac8c195-cb9c-3d57-b662-0c40a950692b | -12.30083 | -44.33394 | 2025-10-09 04:19:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97a1b610-2978-3146-b717-3104069fcb00 | -8.73557 | -41.66301 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5840f92d-e6df-3eec-897d-cc0f3fcfcb20 | -10.85115 | -49.91724 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2c9a7a7-eea8-3bab-ad9d-f91fc6ec767b | -13.79223 | -45.86219 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637263b1-19b8-304a-b160-e57cc5412ddf | -10.19803 | -44.5705 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cef92a86-550f-3dce-a44b-8a06e23864e2 | -10.52268 | -50.02429 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0219457b-4a90-30b0-93cc-6668d3feeab6 | -8.22971 | -44.15317 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 211db8ff-1cb7-3e7c-aa4c-7c90ce255e51 | -13.78396 | -45.84993 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 475696c2-4bca-367f-b4c5-1f5fcd92c241 | -7.81992 | -46.71363 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 753bb753-6e0e-32fe-bd2c-df833feacdc3 | -13.79334 | -45.85509 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ac90141-1573-3dfe-9f03-b96622402d4f | -13.79279 | -45.85864 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a888233-8c1b-3891-8ebc-1bbc3213e155 | -10.65857 | -44.15572 | 2025-10-09 04:19:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1beca5e-268f-38db-8e12-68be51219f68 | -10.81683 | -41.95393 | 2025-10-09 04:19:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6f4a004-046f-3f3f-987b-e88e0075bf7a | -10.89326 | -50.64442 | 2025-10-09 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07a0d73d-d14a-3797-86c4-3fb7ec7b768e | -10.85967 | -49.91376 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6b354437-b36e-387a-81ad-4de1376b1b9e | -10.86985 | -44.28386 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc1ddb2-2ac2-3e99-8558-e294b6081014 | -7.17046 | -46.71791 | 2025-10-09 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d29292ea-60df-3ecb-a80c-c99c3cd73e69 | -10.22712 | -46.08975 | 2025-10-09 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56589398-fe2f-36ab-ae17-059606db2257 | -10.85811 | -44.62672 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| e769087b-9926-399a-8418-c98129104225 | -11.99302 | -45.18814 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b444203-6cec-3940-9aa3-74f61a0c5354 | -7.81971 | -44.16788 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ecf8a15-1577-324d-8c3e-ae8f01c044ef | -9.98804 | -43.59262 | 2025-10-09 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df36944f-c57a-327e-aad0-9ace7a7dcd45 | -7.32469 | -44.79063 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44cdc61f-b2f5-34f0-ad38-c6725ee045b3 | -3.8594 | -41.53064 | 2025-10-09 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fba7e8ff-17ab-3a19-8f96-d5b5054f06bd | -7.17389 | -46.71845 | 2025-10-09 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae70bdd1-6676-3245-8175-ee36541db3e3 | -14.78523 | -46.11189 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f8a573b-4eb9-301d-b644-ba8db10228b4 | -7.77378 | -42.4054 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4015753c-b98e-36b4-921c-09f89aed5504 | -7.63582 | -47.6927 | 2025-10-09 04:19:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e683c03-c472-3689-b945-c6c3cd279fc9 | -8.22916 | -44.15668 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5a8a3a0-b16a-3ed9-b4c2-8772d4d33622 | -8.62364 | -48.60749 | 2025-10-09 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05d35c59-5e26-3f65-b624-6b9706524f72 | -11.98694 | -45.20528 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70b30aa3-56cf-3429-aff0-0ca1b43d0e19 | -8.51016 | -44.22592 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a337c90-004d-3db8-87a5-1ef569089d32 | -10.80214 | -44.0849 | 2025-10-09 04:19:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ace0f85-4168-3a65-92ae-dd747861984b | -8.53895 | -46.21312 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37729971-3009-3c6a-a50f-3dce64e97f5b | -12.06982 | -45.73841 | 2025-10-09 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00432fc6-4ed0-3858-b04b-11d3d48a4642 | -7.80682 | -46.64307 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37e6fd77-3692-37da-83df-ec380736f237 | -14.07363 | -50.15699 | 2025-10-09 04:19:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84ff9d04-5787-3c97-8768-13b39154642f | -12.24526 | -43.7738 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f063649-f454-3e05-8a02-65b2514cd3dc | -8.5201 | -46.18071 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de12ac10-48fd-3c6d-8caa-299dd09fc5a3 | -8.54288 | -46.21008 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 369b23f7-ed44-3ec2-af06-93bede84866d | -11.86949 | -45.52215 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c7a1fc3-7ddf-3155-af7f-d0a31cbb306c | -11.46393 | -43.48156 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a84f7f3-8c1d-3eb2-a09d-0f791dd43b56 | -8.56717 | -44.62222 | 2025-10-09 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 796790fc-a629-3dfe-a619-5ec4fa8d894f | -8.55119 | -47.7242 | 2025-10-09 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6f23312-dc39-3f4a-b6f7-c262779c3dcc | -7.77159 | -44.04201 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0380786b-2eda-3357-9992-169d2f2a2c9c | -13.03046 | -43.9052 | 2025-10-09 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08903f15-b447-365e-93b4-da9b868e594a | -10.85551 | -49.93807 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0d06020-55b1-3888-bdd9-34dd791870db | -10.78583 | -44.07864 | 2025-10-09 04:19:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c901ee10-4c79-3ec4-9ee2-25f854c8b267 | -7.7188 | -42.38159 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7057b01e-0c16-312c-951d-a639fa82bc38 | -10.85866 | -44.62316 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 5e7a8b07-83a5-3b29-b7ff-acace68cff13 | -7.84517 | -41.34571 | 2025-10-09 04:19:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ee0565f-df46-3f84-b86d-854a75c8097c | -11.74838 | -45.14573 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9558ee0b-0563-391f-b311-a23f4e194c3e | -10.86368 | -44.63486 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 03d56af0-418f-35c0-a19d-75490cd1d68b | -11.8739 | -45.53727 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4ac4144-bfa6-3590-889f-18163f446430 | -7.75884 | -44.03638 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a17db40c-7812-31b4-b743-aa9e57dd4ba1 | -7.76827 | -44.04147 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d3a5fd88-baa2-32a3-b734-b000a62e784e | -1.9669 | -47.3102 | 2025-10-09 04:19:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6994da7-f5e4-30c1-ab8a-0368db3747e9 | -8.63526 | -45.15939 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7b65c8b-1894-344e-9f4b-6cbbbc93755e | -7.79848 | -42.61761 | 2025-10-09 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6a5ef34-d7d8-3639-b943-6f4f4f599fb7 | -11.78821 | -45.15208 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92e990dc-7228-36af-a3f8-f826502c2b81 | -9.21989 | -47.846 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99032831-5ae5-379b-9afa-6f0807a0f24f | -7.54843 | -44.29702 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 419957dd-3487-3736-8451-2517a81f609b | -7.80121 | -44.20087 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 56402aaf-6536-3fc4-9310-9bb425ba28e6 | -13.80494 | -45.84607 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8494dbf4-835b-3ee2-9f15-6ac6a7b8c89a | -14.78578 | -46.10834 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af86e056-e971-3c9d-8908-118d55047464 | -3.30172 | -42.09467 | 2025-10-09 04:19:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b53e4d71-2e77-3bbf-a13b-50e390137d31 | -11.77318 | -45.05198 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d6fb973-bf4e-3252-8e2f-68e23913230c | -7.70709 | -44.6704 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2278b1a9-7ebd-3d90-8d7a-a286065da52a | -11.99965 | -45.18921 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4483924d-1314-38dd-becb-d47a3863fccf | -8.196 | -43.33636 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| bfd214d1-4e15-3d20-abc9-090493e51205 | -13.39108 | -42.7018 | 2025-10-09 04:19:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 96193020-6d1d-32a6-a778-254554b66726 | -3.85471 | -41.53781 | 2025-10-09 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 704c94b8-3a58-309c-a296-0cecd36e7c21 | -9.09253 | -47.95843 | 2025-10-09 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cab056d-3fd9-3a26-8d90-d7784b5a96ed | -10.44544 | -46.63671 | 2025-10-09 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README40.md)
