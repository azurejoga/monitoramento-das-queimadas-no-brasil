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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdfb647e-69d9-3784-87f1-95e971375cec | -17.59503 | -46.56581 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46c45555-8181-39a8-8cef-aca7900602ce | -11.32544 | -47.84318 | 2025-08-23 03:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bd47eb5-c0da-3258-8727-6e3c0970eb59 | -14.93741 | -48.01191 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faec94c9-98b0-3e32-bdb8-3bdbc1a69614 | -13.03559 | -46.32294 | 2025-08-23 03:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4633ee83-affa-3333-b023-a44b425fa4f3 | -12.99244 | -45.23458 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c732e4f6-c8d2-30d6-9a2d-6e82a4403070 | -12.54448 | -45.6237 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fece632e-dfa6-34b1-9589-b5aa9302b2cb | -13.0454 | -46.33637 | 2025-08-23 03:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd9b4ef2-55b1-3129-8459-283574e8a3dd | -15.20093 | -48.25457 | 2025-08-23 03:40:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b30da2c2-1cc5-3d77-9102-c1401fd6e7c0 | -15.06688 | -48.49283 | 2025-08-23 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d52b90a-97a6-332b-9d71-5846c7d98b1b | -15.52661 | -41.68379 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e7c4ef0-414d-3733-a22d-49fe65ff92fc | -14.91371 | -47.99671 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b9ff095-3f1c-3661-b531-7d3e11163ace | -13.58227 | -43.35443 | 2025-08-23 03:40:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c10ac318-6aa0-37f2-80f3-c897fcee6889 | -14.47397 | -46.05488 | 2025-08-23 03:40:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2c08448-bc1d-3045-8bca-f974431f9e67 | -15.56219 | -42.6855 | 2025-08-23 03:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d3ac25a4-f373-37de-b43f-600822e29fc2 | -12.99808 | -45.23574 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2abc6655-1289-3afc-8c55-fd3cd09ebbc2 | -15.56097 | -42.68745 | 2025-08-23 03:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8c251c6e-22d7-3af5-89a9-79390837a7a4 | -14.78903 | -45.49484 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4886a2a1-cc17-320b-a6b2-aa95d7bf0bb9 | -11.13855 | -44.74633 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 347ca450-aa1e-3e63-ad67-b857cae308c5 | -11.05861 | -44.60384 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14469cf7-2ad2-3772-9cc4-b80358d0718c | -11.44593 | -47.32876 | 2025-08-23 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1998e6aa-7629-3942-9694-dcfe4404311c | -18.2825 | -45.57289 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 962117dc-e736-3cff-afd5-4c38e122a000 | -12.54362 | -45.62794 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc807526-7653-3f64-af41-da2b70f07492 | -18.27802 | -45.5682 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1587b019-8e05-310b-bd2d-fa6ed70b1969 | -17.27539 | -46.77296 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4866c72a-4c33-39b5-bdd7-81f5d313cb2d | -14.78824 | -45.49865 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3404af2-a740-3b0a-9cb9-713b4b64557c | -15.55853 | -42.67977 | 2025-08-23 03:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 310427fd-a346-377d-87f8-06d1ad80029b | -12.98758 | -45.22948 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e78f3ac8-2570-3d12-9165-25488d5feb44 | -13.16548 | -46.92279 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6159c645-e459-336d-888a-7930a0581679 | -18.25173 | -45.56803 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97d1431f-fda8-3e07-9742-5e6b85f83508 | -17.59041 | -46.56885 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57e9add4-3306-37ef-92c5-1980d348ed5f | -17.58654 | -46.55957 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31587161-8d5d-3ad8-8b36-e8ac1e1ce6a8 | -15.56121 | -42.69076 | 2025-08-23 03:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bdd6cd8a-645a-330f-a8a6-793789d39810 | -14.81553 | -47.95258 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 99fc1ae9-7875-3a56-a32f-aaca68623ee4 | -11.13408 | -44.76958 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 713ce98c-620f-3884-8236-e24f6c386404 | -18.30084 | -45.56348 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17a6c09b-c63a-3877-a1fb-c06af7aa46a5 | -17.59688 | -46.56624 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f0ed635-0c71-3191-99d3-74875de39243 | -14.80861 | -45.45619 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59eb171d-2a1f-3b9f-bf74-d9b72aa91743 | -15.07343 | -48.49454 | 2025-08-23 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 274d476b-c61f-382e-8593-9ce6965bf070 | -14.79681 | -45.42968 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b602916-e5e0-3788-a491-59961e0921cc | -12.99321 | -45.23064 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d35f866f-f313-3a7b-b701-1ee9a3666e0a | -14.82182 | -47.95458 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c833491-50cd-3c5e-928f-a59602a7b559 | -13.39695 | -46.34838 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feb978b6-97a1-355a-a081-fd372305294d | -11.13482 | -44.76572 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9cfbf267-5818-381f-94b6-00e50345205b | -14.81663 | -47.94758 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e60da91-5160-3cf8-97fd-a99aeeff1242 | -14.78531 | -45.49549 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03d07719-8986-3ad0-a6f7-97f585b0cfc3 | -17.70361 | -48.51363 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1c6c2a5-f4a8-3790-9d97-430cb19134f1 | -14.94168 | -48.02061 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b785a56-f653-387e-b91f-7ab863e36a3f | -14.78221 | -45.39626 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c5f10c1-329e-31bc-8d6b-053df9614d79 | -15.53139 | -41.69143 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81bdf0ce-edb1-3822-98b2-4457d62e4019 | -13.3813 | -46.21218 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3f100fd1-0e44-36ac-b0d3-c7e2d0c24209 | -18.30423 | -45.5472 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2e5d2e4-a554-3f83-9ebf-588e1a4898e8 | -17.27152 | -46.76307 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f950cb7-bfa8-3970-bab3-689e91a745c8 | -11.32467 | -44.95845 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e105a537-6d7e-3e26-b528-3fb38200bb04 | -17.04769 | -47.14063 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d360a60b-b1e0-30ee-a2cd-8336f45e854b | -14.80942 | -45.45231 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f51e517-3381-361f-9dd8-ed0c5cddc2be | -18.25122 | -45.5658 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c763856a-0500-33c4-9962-c35a7b4308ef | -18.25311 | -45.56127 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b1cfc46-10cd-35b2-8260-4529d3067a64 | -14.77746 | -45.39133 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a6138be-25b2-3fca-af9a-562a8bcc9f40 | -13.00216 | -45.22746 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8451d422-294d-30c2-a269-170ea66d868c | -11.13631 | -44.75798 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f6f043b-e122-3eda-81bb-d349ea12b9c0 | -13.72586 | -44.40203 | 2025-08-23 03:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78477eb7-6e7a-3f54-96af-2d793e6badca | -15.71247 | -41.92639 | 2025-08-23 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| fecf61df-fb9e-37df-91b7-50d2ed697376 | -17.59387 | -46.55297 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 133b409a-428c-34a1-b088-1376af90616d | -13.00038 | -45.22401 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a5369b3f-a090-3f4c-88cf-15472784b12a | -14.82808 | -47.95675 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aec7df2f-4a4d-3c07-854c-7b761a0555b4 | -18.68264 | -41.19623 | 2025-08-23 03:40:00 | NPP-375D | SÃO JOÃO DO MANTENINHA | MINAS GERAIS | Brasil | 3162575 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c6f5b2e3-5af1-3622-bb3b-0009e94aefde | -14.91746 | -47.31709 | 2025-08-23 03:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0d166c4-a264-3115-9a2d-61c79a15824e | -13.64752 | -46.8896 | 2025-08-23 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7b99435-8e91-38aa-84af-5ea16dcdef55 | -11.13254 | -44.77761 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7be01ad4-ad6b-35f5-b34f-f55ea095bf18 | -18.29324 | -45.54765 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f74c16a-cb72-369f-930e-58c617220b31 | -14.82727 | -47.9601 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 372f5713-0c19-3d77-90dc-d8d71d59228d | -13.32953 | -40.34346 | 2025-08-23 03:40:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 10f608bb-a110-3b68-80c2-db8573c067fa | -11.98425 | -40.86682 | 2025-08-23 03:40:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 76f0c63f-2a3d-3467-9328-abbe6c070477 | -17.70053 | -48.51709 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e2714d0-341b-394a-b3a9-ce24bd4d77dc | -18.05189 | -42.95559 | 2025-08-23 03:40:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 92891897-34ab-34e8-81ba-8f8a9efe5ba6 | -13.64617 | -46.88578 | 2025-08-23 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db674f96-263d-30c1-8837-e9c56da5571e | -18.24978 | -45.57257 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9e863ab-7e02-376e-bcd7-e85813c64d4f | -15.55757 | -42.68491 | 2025-08-23 03:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1599bc52-5710-3ce9-b45a-39aeea4ea358 | -13.37828 | -47.51132 | 2025-08-23 03:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 822da1cb-dc05-37ed-b86e-7265c9e21d3a | -18.25103 | -45.57142 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 124a8e23-6771-3ced-9cbc-568304257f8d | -17.58382 | -46.5631 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b056c36-6d70-3471-bf49-3366d31d6558 | -11.05374 | -44.5989 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 032d3bd0-7dd8-3bb0-82c5-a64e5f367845 | -17.60943 | -46.69967 | 2025-08-23 03:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5208f104-5afb-31f5-ab99-a43dfc4b1dad | -12.99399 | -45.22672 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3d1d1d9a-f33c-3673-8a12-ef53ea5e8818 | -13.37301 | -47.5044 | 2025-08-23 03:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0aee7508-91c3-37c1-b789-d530dd745f1a | -11.4448 | -47.33427 | 2025-08-23 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 241a943a-0dde-305e-acc8-e73206ea3b53 | -18.28179 | -45.57624 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f241b5f-d76b-3eec-8533-12ff573f8cd8 | -18.26095 | -45.57141 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1f34617-02ff-389c-b1b0-f707a98edcfc | -12.70345 | -48.10708 | 2025-08-23 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6fb61399-3396-3cde-a277-c7ffb0571660 | -14.78511 | -45.48591 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a5b9cb9-60ff-3663-85b5-c8e7d23dec52 | -14.78696 | -45.40121 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| effde8c8-fd81-35f9-a544-06849f28979d | -17.59027 | -46.56047 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f45453b1-c14a-3d26-9205-2780546cad3f | -16.33189 | -46.77784 | 2025-08-23 03:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b09e5ae0-6676-3a7a-82be-2da1ec35fef7 | -14.78591 | -45.48206 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a0958ce-03a1-321e-9a58-2f1e48ef1bb2 | -17.28105 | -46.77457 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a594649-b87e-35ff-be00-dd950474da82 | -14.79815 | -45.43146 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c7a0764-e630-365e-bd71-43dc5024610f | -14.80321 | -47.94673 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8cc7e603-da16-37ca-848d-7a919574b91f | -14.80411 | -47.94328 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c88edbc7-fe5a-347c-81e9-69f9b6db793e | -12.99885 | -45.23183 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e08cbe35-e23b-3050-a2f9-acbb209d1226 | -14.47307 | -46.05923 | 2025-08-23 03:40:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README17.md)
