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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 105d440c-378a-369f-b68c-026f0f7b6d19 | -22.22747 | -47.57715 | 2024-09-26 00:39:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 34f29f51-c7cf-3a3f-b3d8-32e361b9520f | -22.21542 | -47.57823 | 2024-09-26 00:39:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4ea9b944-855b-34fe-aad7-5db6a44156f7 | -22.21347 | -47.55984 | 2024-09-26 00:39:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| cd7e1936-71bf-3d23-9f36-8199b2b4556f | -22.17586 | -43.44269 | 2024-09-26 00:39:00 | TERRA_M-M | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4ee83018-3470-3e03-ab23-007548fec9cf | -21.94178 | -48.57049 | 2024-09-26 00:39:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 3a233423-4549-3218-a1c1-46a78f8d4ecc | -21.92883 | -48.57158 | 2024-09-26 00:39:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 281.1 |
| 391ca184-8ca3-3c47-8d66-7d570069353a | -21.92672 | -48.55035 | 2024-09-26 00:39:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 206.4 |
| cfb96984-169b-3497-a052-165687952ef2 | -21.73722 | -41.55518 | 2024-09-26 00:39:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| e4c01a4c-0207-3b60-9807-e4f22031d0fd | -21.39691 | -42.96657 | 2024-09-26 00:39:00 | TERRA_M-M | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 110fc7ea-34bd-3348-b2c3-524c2eb9ac39 | -21.37465 | -43.63728 | 2024-09-26 00:39:00 | TERRA_M-M | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 785747ef-0144-3fa6-af98-a5faee590645 | -21.37333 | -43.62708 | 2024-09-26 00:39:00 | TERRA_M-M | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| f3a3ba80-1b4d-3172-acb6-2b2447cdd391 | -21.3354 | -43.4069 | 2024-09-26 00:39:00 | TERRA_M-M | ARACITABA | MINAS GERAIS | Brasil | 3103306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 2100e0bf-646e-34ed-830c-be48b6bffa94 | -21.21027 | -45.75855 | 2024-09-26 00:39:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| ff67ed21-e1b2-32f4-8472-db2777076aa0 | -21.1749 | -42.07811 | 2024-09-26 00:39:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 04968178-0705-3d89-a7ee-6a9073c9a773 | -20.9989 | -41.28823 | 2024-09-26 00:39:00 | TERRA_M-M | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| d1a82e76-f5e2-37e5-a78a-b4142dbf26f9 | -20.99753 | -41.27858 | 2024-09-26 00:39:00 | TERRA_M-M | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ff356a29-e1a6-3ca6-936d-025f6b563190 | -20.9796 | -41.40829 | 2024-09-26 00:39:00 | TERRA_M-M | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 204fbc4c-7508-37dc-920a-7e48647b8d56 | -20.97825 | -41.39878 | 2024-09-26 00:39:00 | TERRA_M-M | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b743ad31-8c37-3926-bff4-139e1560306d | -20.77131 | -42.21536 | 2024-09-26 00:39:00 | TERRA_M-M | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b5abc656-180c-36a2-96e2-843638385ee3 | -20.64544 | -41.07138 | 2024-09-26 00:39:00 | TERRA_M-M | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| ac641bbc-5c63-3003-b59d-ceb04a9bd7b5 | -20.64407 | -41.06197 | 2024-09-26 00:39:00 | TERRA_M-M | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 3c230cff-00c4-3c84-8344-e1cab41840b9 | -20.62908 | -41.21112 | 2024-09-26 00:39:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1cc7f341-5ebb-3b95-a863-a3382d3699cb | -20.6067 | -41.25025 | 2024-09-26 00:39:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| b019075e-4faa-35d4-b30b-31e7cc533244 | -20.60534 | -41.24084 | 2024-09-26 00:39:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 5755c7a8-7dfc-3386-be11-094beb0e2c13 | -20.59641 | -41.24236 | 2024-09-26 00:39:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0d85d228-1ae3-3742-85bd-7cea29b50c82 | -20.59502 | -41.23268 | 2024-09-26 00:39:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 2c140797-bc92-30e2-b2c3-0191d6d0779a | -20.46844 | -42.16282 | 2024-09-26 00:39:00 | TERRA_M-M | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a510a3ae-6012-3866-9d18-1bc0aa90ec2a | -20.43988 | -42.02311 | 2024-09-26 00:39:00 | TERRA_M-M | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 3f05b8f9-dfbc-3213-a136-d9529ed32dc9 | -20.42896 | -41.88053 | 2024-09-26 00:39:00 | TERRA_M-M | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| aadac7b5-5b51-36ac-b82c-f69fa0b1d366 | -20.4201 | -41.88191 | 2024-09-26 00:39:00 | TERRA_M-M | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| 2b5e494e-ab19-3315-9edd-2b70c770f776 | -20.41878 | -41.87254 | 2024-09-26 00:39:00 | TERRA_M-M | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| 66845986-d5a9-3ec4-b67c-ba0bf8918b76 | -20.41124 | -41.88334 | 2024-09-26 00:39:00 | TERRA_M-M | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| c1fa66b0-6b59-3aa1-b905-04444050ffcc | -20.40991 | -41.87399 | 2024-09-26 00:39:00 | TERRA_M-M | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 757f6c87-8cc9-37d3-9cfa-05a54ee1a6cb | -20.40237 | -41.8848 | 2024-09-26 00:39:00 | TERRA_M-M | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 170af7c0-51b5-3d3f-a029-9fc8870d6bdd | -20.40105 | -41.87546 | 2024-09-26 00:39:00 | TERRA_M-M | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| c8ad13d2-acc6-3f1d-b717-77a59b70528b | -14.86791 | -51.52429 | 2024-09-26 00:41:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| bc706bf0-28ad-3bb8-9eff-b4f9135adbfc | -14.86504 | -51.49697 | 2024-09-26 00:41:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d8b1cd59-5ff4-3a3b-9a16-0e16e70f8cef | -14.86373 | -51.50357 | 2024-09-26 00:41:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 391daf7f-a3c8-3ff7-b3db-aa34cacffc1e | -13.74707 | -51.09714 | 2024-09-26 00:41:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b394f200-4fe4-3bbb-8ba2-c78d08338f17 | -13.74438 | -51.07291 | 2024-09-26 00:41:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1b24f22a-5156-319a-8728-0bd2008c2827 | -16.01043 | -48.1661 | 2024-09-26 00:41:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 723daa06-92a0-377d-87c5-14cf5b2910ab | -16.01056 | -48.15602 | 2024-09-26 00:41:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 421bbf15-19af-3606-a955-61899bfae2fd | -16.01245 | -48.17165 | 2024-09-26 00:41:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 48986844-1ef9-3007-a0f9-799f64ba3883 | -16.04031 | -43.61837 | 2024-09-26 00:41:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2d89b833-dfa5-38ba-8423-95a0dca4e1a6 | -16.09582 | -51.99586 | 2024-09-26 00:41:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 35.0 |
| cbcb78b9-bc08-375c-acc3-5f5140954bd5 | -13.31991 | -46.34193 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d850ad9c-afaf-3b76-af56-67bd69b5825d | -15.91223 | -45.00246 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b5c81e6a-1746-3752-bbce-6527cf8f557f | -13.53445 | -42.56591 | 2024-09-26 00:41:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c5175c97-d4d6-396e-88c5-7e4721596dea | -13.31712 | -46.31988 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 36584fb5-4fae-3635-9db5-2a9159b8e87d | -13.31642 | -42.45843 | 2024-09-26 00:41:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1a8645d1-0f1b-32b0-9558-cd5b4764bb1f | -13.31586 | -46.33771 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fba9e316-fc1f-35ec-81e8-31c8cb620f64 | -13.31508 | -42.44905 | 2024-09-26 00:41:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 52d01dfa-f5e7-31a2-a3bc-388206a12600 | -13.31439 | -46.32664 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 143f6ac2-32e5-357a-abe3-79001db5f744 | -13.31166 | -46.12463 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 41b8d699-9b75-3e1b-aa0b-66c1515a12ac | -13.53312 | -42.55657 | 2024-09-26 00:41:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 042b82c0-1ffb-38d5-9be9-ebebadd6f049 | -21.2807 | -51.01661 | 2024-09-26 00:41:00 | TERRA_M-M | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.5 |
| aef46934-b853-3637-a146-b0b632449471 | -20.92161 | -49.68449 | 2024-09-26 00:41:00 | TERRA_M-M | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 5c9528cc-0e5b-3225-a25b-93481e87e5cc | -20.82227 | -47.22945 | 2024-09-26 00:41:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 633e85f1-ffe9-36e7-a233-87661ff6d11e | -20.68214 | -45.0064 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7879544c-d7ad-3b46-b7c8-35f5b8ad93f3 | -20.62145 | -51.49839 | 2024-09-26 00:41:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.9 |
| bb7a435a-c2d4-36d5-ba78-dd7ed5a23166 | -20.6155 | -51.49243 | 2024-09-26 00:41:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.3 |
| 7708a7d5-aad7-36e2-adaf-aa19b5029b7d | -20.6057 | -51.50048 | 2024-09-26 00:41:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.6 |
| 7dab2f3c-6719-37bd-ba50-5f3dd7adb93b | -20.60261 | -51.46612 | 2024-09-26 00:41:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.2 |
| d16ed97c-86c5-3bfd-ad42-b8488d25be36 | -13.31031 | -46.11416 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 60510e83-98d8-3b57-afbf-02ac9b841813 | -20.59974 | -51.49459 | 2024-09-26 00:41:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 175.2 |
| 0496e99f-c75f-3d9d-9581-081d93f54385 | -20.59691 | -51.46018 | 2024-09-26 00:41:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.3 |
| c63709e9-aa61-334f-b83d-e5b24f3403bb | -20.58686 | -51.46791 | 2024-09-26 00:41:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 21f34350-7868-37b3-87d2-7774ab8fb806 | -20.52399 | -43.94036 | 2024-09-26 00:41:00 | TERRA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 67ed4368-d544-3c47-8f54-f6d60dbe78c7 | -20.52265 | -43.9301 | 2024-09-26 00:41:00 | TERRA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 2634b716-4751-384a-b13c-4dd36c694b76 | -20.45789 | -44.01326 | 2024-09-26 00:41:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| bbfb08a1-2ec3-367e-89fe-eb4a3bf99d74 | -20.45658 | -44.00294 | 2024-09-26 00:41:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 166b1ae1-c9ab-3c2b-974a-cb825a1964b6 | -20.45071 | -44.00975 | 2024-09-26 00:41:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| a19ec666-0ed2-39bf-8ddd-4913658e6eca | -20.42557 | -44.10797 | 2024-09-26 00:41:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 37b32699-9733-3630-9859-1d8b9fed257a | -20.33982 | -41.90076 | 2024-09-26 00:41:00 | TERRA_M-M | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 11f94d7b-a255-3ca1-b63a-29fde7ffe8cd | -20.30302 | -41.25181 | 2024-09-26 00:41:00 | TERRA_M-M | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| 0497f655-1665-34e0-92af-0c14eaae5471 | -20.30164 | -41.24231 | 2024-09-26 00:41:00 | TERRA_M-M | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 4b9f61d4-3eca-37b9-9106-a1227a3879b9 | -20.28719 | -41.46513 | 2024-09-26 00:41:00 | TERRA_M-M | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| b224616f-1d9b-34eb-83ab-d476d0969fe6 | -20.27829 | -41.46653 | 2024-09-26 00:41:00 | TERRA_M-M | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 33.8 |
| 2368edc0-e72e-33c7-8e03-06bb58d75671 | -20.27745 | -42.71319 | 2024-09-26 00:41:00 | TERRA_M-M | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| bf16f296-fdfa-3579-b09b-e9f0d1ecb30b | -20.27695 | -41.45721 | 2024-09-26 00:41:00 | TERRA_M-M | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3f11ae6c-2334-352c-a390-6a982875cb07 | -20.27615 | -42.70371 | 2024-09-26 00:41:00 | TERRA_M-M | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 0f01d6c8-6739-3608-90b8-50fd78f030b9 | -20.2627 | -41.29393 | 2024-09-26 00:41:00 | TERRA_M-M | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| f26da3d4-975e-3635-8b2f-fc49fb6bc63c | -20.26132 | -41.28437 | 2024-09-26 00:41:00 | TERRA_M-M | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 84be5ae8-7b62-3358-b0f3-fa8508805034 | -20.25097 | -44.17784 | 2024-09-26 00:41:00 | TERRA_M-M | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e3db1012-cb47-34c5-aed8-20728b2ff08e | -20.21062 | -43.44706 | 2024-09-26 00:41:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| f6d42a52-e6a8-32fb-b05f-63caf57b1a95 | -20.20933 | -43.43722 | 2024-09-26 00:41:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.5 |
| 8da3a2a0-771a-3bff-81bd-aaf2cff96551 | -20.18715 | -43.54512 | 2024-09-26 00:41:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 0bdfc19c-1367-34c7-8972-2c6dfeba44e5 | -20.1859 | -43.53561 | 2024-09-26 00:41:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 9ec4b2a1-13aa-39ad-b4fc-e1d88f03fea9 | -20.17031 | -43.55777 | 2024-09-26 00:41:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| c4260257-653f-31e6-b1b1-ff263ce42ab9 | -20.16127 | -43.55937 | 2024-09-26 00:41:00 | TERRA_M-M | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b5347d6e-242a-3c39-bf04-befe4bc7a0ef | -20.15744 | -46.59402 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7470bb72-9dd7-3ae9-bbb9-3d9194b36994 | -20.15739 | -43.52987 | 2024-09-26 00:41:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| f0999029-c56d-3519-a741-d9913c72eaa6 | -20.15615 | -43.52046 | 2024-09-26 00:41:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ab8bfb18-a287-3933-a6ab-f805f13e0627 | -20.15229 | -44.34839 | 2024-09-26 00:41:00 | TERRA_M-M | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 3b484583-adb8-312f-80a8-342397b9196f | -20.15093 | -44.3376 | 2024-09-26 00:41:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 33d1e391-d93d-350b-810b-8f0971d719d1 | -20.12419 | -44.27669 | 2024-09-26 00:41:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 19f9bab0-d324-3ca7-862f-948fe6d53af0 | -20.11851 | -43.44478 | 2024-09-26 00:41:00 | TERRA_M-M | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| c82fc94e-68a6-392d-b707-ee9956f33aac | -20.10826 | -44.27401 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 81f1e6ac-268e-3304-b135-3820422ca506 | -20.10432 | -44.24342 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 80daecd7-7c92-3436-8958-ac4caaf6dca2 | -20.03912 | -45.6688 | 2024-09-26 00:41:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README10.md)
