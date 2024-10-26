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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45dbeb6-6105-33a5-aa7a-d411041f60c6 | -18.1598 | -42.45842 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6a07b7c9-1d10-342b-b18a-db64af4d14bb | -18.13022 | -42.23864 | 2024-10-26 03:57:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e178fbb5-e76a-3f65-b95e-8377fd4c6113 | -18.12961 | -42.24237 | 2024-10-26 03:57:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 13fd6abd-0998-3542-b0ff-de06c1fa4a8f | -18.12626 | -42.24179 | 2024-10-26 03:57:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e794b5b5-3907-3537-af43-0baad768e4ad | -18.09171 | -42.18639 | 2024-10-26 03:57:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e2deb3a9-5fac-3601-a12e-a2e61912deae | -19.915 | -42.32257 | 2024-10-26 03:57:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 20cbf42c-66e1-3219-bfa6-9f5909a29805 | -19.91168 | -42.32199 | 2024-10-26 03:57:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 608a6ba9-2052-334f-a14f-592681516429 | -13.57181 | -43.4263 | 2024-10-26 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5340df17-bdcc-3f85-87ed-a698def15f28 | -13.05823 | -43.35189 | 2024-10-26 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5410eae-4767-331b-b5c0-5975d1580b6a | -12.92365 | -42.44601 | 2024-10-26 03:57:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 36d43686-2e63-30d0-a2c5-57ffabb6b37b | -15.00225 | -43.35348 | 2024-10-26 03:57:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d66b14f1-b89f-3c52-9ca7-bf3a1f01155b | -14.66609 | -43.10867 | 2024-10-26 03:57:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 488f078d-1e0c-304d-b2c4-4b244ec8ed34 | -14.55388 | -42.97586 | 2024-10-26 03:57:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47a47e3c-80b8-3d75-8d45-2e55b130ecd5 | -14.5532 | -42.97992 | 2024-10-26 03:57:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 688e76c9-14ff-3c47-9d06-9b0583c58ee5 | -14.55037 | -42.97519 | 2024-10-26 03:57:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d3411d4-50f3-3945-b300-9c5b40083961 | -14.54968 | -42.97925 | 2024-10-26 03:57:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10bce8bb-c5bc-329a-989c-15ede265f1ce | -14.4459 | -42.44496 | 2024-10-26 03:57:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2efc3201-9614-3603-998f-9e0c789ff435 | -14.1417 | -42.89849 | 2024-10-26 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01862971-d0ee-3766-858d-4c8613c1ce1b | -13.83014 | -43.23497 | 2024-10-26 03:57:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6423487e-8f1d-3a57-8187-7465abf0d854 | -13.81117 | -43.34597 | 2024-10-26 03:57:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9d6d1120-46b1-3e71-b979-69f1c525bda5 | -14.89513 | -43.55789 | 2024-10-26 03:57:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0753b806-866b-3518-b507-19da420a4820 | -14.34731 | -43.61809 | 2024-10-26 03:57:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3841cf4e-9c7d-30a6-a98d-1c012e638e67 | -15.77849 | -43.06755 | 2024-10-26 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af621a29-923d-3f68-93ba-3e0a73683849 | -15.67078 | -43.29237 | 2024-10-26 03:57:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 095370f5-d6eb-33f1-970d-8dca0e98f75e | -15.50869 | -43.17611 | 2024-10-26 03:57:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 194b9746-fe05-3746-a934-6600b7a42ef3 | -15.26705 | -43.05889 | 2024-10-26 03:57:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f88493c4-43aa-31bb-9d89-41e7e456f3c4 | -16.04385 | -43.72623 | 2024-10-26 03:57:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb2e5e49-2eab-336c-8cf5-7675c1a35144 | -16.04027 | -43.72556 | 2024-10-26 03:57:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaf6fbd4-7a12-3520-8d0e-b7274d992342 | -15.96028 | -43.55565 | 2024-10-26 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32fc82ec-34ee-338b-8fcb-fec98f08ea79 | -15.83222 | -43.60236 | 2024-10-26 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1af1a861-34a0-3392-9042-25b557dd0fba | -15.61019 | -43.7318 | 2024-10-26 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3d2b1629-d30d-3732-9b7b-25a5203dd2e6 | -15.57101 | -43.76476 | 2024-10-26 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0f0d1c6-a521-3d2f-9110-da273250b212 | -15.45792 | -43.61682 | 2024-10-26 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08517970-eaf2-3275-b7e2-d1812ed1eb16 | -15.45677 | -43.61361 | 2024-10-26 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c25bf6a6-2ac5-31c3-9550-14674afb1c67 | -15.45604 | -43.61789 | 2024-10-26 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26060d2f-0102-3737-8bd4-822ac2a9198d | -15.30216 | -43.70663 | 2024-10-26 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a79f903b-2fd0-302f-b00f-f3a824f628b0 | -15.30142 | -43.71095 | 2024-10-26 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6d512d6d-f88d-3dbb-8ae8-1862da3af78b | -12.23143 | -43.30909 | 2024-10-26 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50379685-6b48-3131-b152-ba05ebf2bf57 | -13.6668 | -44.29352 | 2024-10-26 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe286726-4802-3de8-aeb5-a5a54d3c175d | -13.61475 | -43.98745 | 2024-10-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 545742f6-6201-3a23-a9a2-0777497ba4de | -13.611 | -43.98679 | 2024-10-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d2d397cb-65bd-36f8-96a8-a9938fdab734 | -13.57011 | -43.74584 | 2024-10-26 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecb87690-f988-3cab-a44a-0e3712853f89 | -13.53891 | -44.65705 | 2024-10-26 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04863177-9431-3cd6-b9d7-c340124ba2fa | -13.5382 | -44.65991 | 2024-10-26 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 220c7a6a-d687-3852-874a-089c198d3ce3 | -13.538 | -44.66216 | 2024-10-26 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 530515e9-a1ba-355a-8c39-e4695ddceef9 | -13.47553 | -44.02717 | 2024-10-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da837857-3bea-3c50-bb36-2dd52202c07c | -13.45569 | -44.09636 | 2024-10-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e933e5df-478c-3360-8913-72d03fec4463 | -13.43007 | -44.3555 | 2024-10-26 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1a78cb9-0968-34dd-b03f-6aa65e40bc8a | -13.35758 | -44.25957 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7cc2196d-c994-3674-ac42-4d02f6400a79 | -13.35674 | -44.26443 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17069525-890e-31c6-b8bf-c9a453ce49bd | -13.28851 | -43.96027 | 2024-10-26 03:57:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72a81a1e-422c-3258-97a9-03d6f43ce74d | -13.28475 | -43.95954 | 2024-10-26 03:57:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25aa1e24-0a4b-35c0-a5c1-c221d0d6e5c8 | -13.2404 | -44.46812 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b33c7bc8-f9e3-3bb8-b2eb-ad65ab4323bf | -13.23168 | -44.63578 | 2024-10-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7bf2bd3-db92-3084-85fc-08bf09b3ffb9 | -13.2182 | -44.57377 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b20cc13-6a3c-3912-8d05-9cb3a07c32e5 | -13.21817 | -44.57598 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d2e4ea2-2870-3728-8734-ff270c6e3806 | -13.01982 | -43.75576 | 2024-10-26 03:57:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b34c710-955b-3da8-a906-58e874acb3f0 | -12.86376 | -44.61712 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b16dfb3b-5e8a-347b-8c91-4bbe5c4f24f3 | -12.75416 | -43.89869 | 2024-10-26 03:57:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28172f36-dfa6-3002-8529-94381a501413 | -12.71345 | -44.3928 | 2024-10-26 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84e3660b-8540-3c52-9759-10c7530a5a8d | -12.71256 | -44.39782 | 2024-10-26 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f763f5f7-e7b7-3c4b-94d1-afba5a53f67f | -12.71234 | -44.39547 | 2024-10-26 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9c9f096c-7115-3381-a82e-47a94a05a5dd | -12.44678 | -44.4156 | 2024-10-26 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4405636c-2c59-3c6a-acbe-66a22c147149 | -14.8385 | -45.18553 | 2024-10-26 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9516211-db88-3bbc-989f-bbf0f73c8198 | -14.24941 | -44.14462 | 2024-10-26 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 813c929b-c351-3ff2-9005-1a8e4341f1f5 | -14.19826 | -43.71965 | 2024-10-26 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d152c02d-daaf-343c-9f61-52c891a2f3bc | -14.12068 | -44.38908 | 2024-10-26 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5e5c948-46c2-3e6a-a561-ef0ffc919518 | -14.11743 | -44.39025 | 2024-10-26 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16e86c42-ec55-383b-b913-b3c7b29e2c93 | -14.0614 | -43.70587 | 2024-10-26 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00173e84-e0d9-38cf-bf6d-41a29426927a | -14.06063 | -43.7103 | 2024-10-26 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59da8ab9-68c0-3420-94e9-759d1fd13a8a | -14.00284 | -44.10825 | 2024-10-26 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 795448aa-71ca-3cb3-9648-5515a9e85ef5 | -13.86302 | -44.46401 | 2024-10-26 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d00f4f3-297a-3470-9634-72ca47a125bf | -13.83766 | -43.73781 | 2024-10-26 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a25348-7c39-3a31-bd92-09e84f19a1b4 | -12.266 | -45.66581 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa8ee3ab-5a81-3291-b910-1e69bc175f1f | -12.26594 | -45.66179 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| caf74d7a-ebda-30e5-bfef-df14ca3195c4 | -12.2652 | -45.66584 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 89cdd487-2487-3283-af86-4882d5d1ee68 | -12.26319 | -45.65688 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b698ea0-1dac-3345-91d5-c09955436a0a | -12.26248 | -45.66092 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 70c9647c-941d-3db6-be61-1b2ca447693c | -12.26245 | -45.65694 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b242f387-9a6c-3674-956b-63cd85bbeea4 | -12.26177 | -45.66498 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 13d129a7-7b47-32d5-879d-98919c929a99 | -12.26171 | -45.66097 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 40b63f1a-bf87-349b-a583-5d239f57bc4c | -12.26096 | -45.66502 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 303ac370-abdd-3420-a288-8188ab40453a | -12.25896 | -45.65606 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| becd15bf-5469-3abf-b8f4-1a2095cd66f0 | -12.25824 | -45.6601 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d27f968f-060d-39fe-bdc1-681f6134efea | -12.25753 | -45.66415 | 2024-10-26 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2f9df4f3-c164-3843-9ef2-d5327b33a576 | -12.10051 | -45.71248 | 2024-10-26 03:57:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebd6690e-8c8f-350d-9309-6dcf4363a16c | -12.09977 | -45.7166 | 2024-10-26 03:57:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e7e45b7-dff4-3111-aaf0-ed1c0d9d5a1e | -12.09771 | -45.70347 | 2024-10-26 03:57:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7e174084-42bf-36a7-9013-92999155212a | -12.07771 | -45.71654 | 2024-10-26 03:57:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9aa9c96-a8fa-325a-b9a8-560cebd935b8 | -12.05687 | -45.73404 | 2024-10-26 03:57:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99b00cad-5774-338d-8d72-51db80874d1e | -13.3327 | -46.37593 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f4fe04f-be01-3691-a3fc-21fdb23bf01b | -13.33198 | -46.37733 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 738bd279-cb05-314f-8d2c-a230e15ee21e | -13.33188 | -46.3803 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b7a4ad1-c88c-33fa-a6f9-e7e5984cc89e | -12.48456 | -45.24816 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9879b390-56db-3575-aabd-f019f6e373bc | -12.48387 | -45.25198 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d1982b3-6f13-35d5-b41a-c904285778ac | -12.48043 | -45.24746 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67dd11a7-4465-3eba-96d5-3c2a7a2682ee | -12.47974 | -45.25129 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6073a99d-c9d9-3fc3-a94a-781e5225eaa4 | -12.47905 | -45.25511 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5eab6a4b-29ea-39ea-bc37-46888d0e76c2 | -12.47493 | -45.25441 | 2024-10-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17123bd1-8f04-3b24-9399-b7634160c128 | -14.70474 | -46.27315 | 2024-10-26 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
