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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c9f0e71-cd0d-30d5-ba44-71345bfc050c | -19.74595 | -46.50267 | 2025-10-04 03:55:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 319493c7-ea74-3250-be0d-5e11a32adafa | -21.19702 | -45.14085 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b0b31367-e4ca-309f-9129-8270f560a1b6 | -20.41396 | -44.1373 | 2025-10-04 03:55:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 39002e5f-2b17-342b-85e1-91b8cf319437 | -18.3135 | -44.04333 | 2025-10-04 03:55:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 012026ef-0b59-3921-a8ed-6b1b1b95b036 | -19.97301 | -43.70575 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 15e7aa23-a59f-3703-9e1c-6f3f14de1209 | -21.27333 | -45.05532 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c70619c5-584d-324e-8b8c-1398824216a0 | -20.72101 | -49.61086 | 2025-10-04 03:55:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 779914a8-63da-3281-a29f-7d75e6308d9c | -18.17161 | -53.34276 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ef02b18-53b2-3710-b65f-ef32177679a1 | -21.01978 | -45.95182 | 2025-10-04 03:55:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3748f627-81fe-3298-bedf-c98e09bd302d | -20.4929 | -43.79022 | 2025-10-04 03:55:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6e2b9f1a-e2f0-3851-8bdc-4b81ade4efc3 | -22.37325 | -47.05896 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b78dd66d-8030-3a50-9df5-31fd35bba8a4 | -19.46733 | -43.64507 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8671382e-e05b-3e2a-97da-5ebd9eff79dc | -17.71039 | -47.08919 | 2025-10-04 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b5bb4986-bed4-3549-aea6-f7338df66ce6 | -22.0738 | -42.10838 | 2025-10-04 03:55:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 173173ef-2f19-3c08-8e0f-28ccfe7f3db2 | -20.13053 | -43.99184 | 2025-10-04 03:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bbe84e90-d133-3e78-bd82-cd75bc42c979 | -18.38709 | -48.79121 | 2025-10-04 03:55:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8a5dd250-9427-3401-a73c-e9d5d31c0a81 | -19.8898 | -42.6249 | 2025-10-04 03:55:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ae58408c-0dbc-3b96-a427-4270de7bd8c2 | -18.72791 | -41.61676 | 2025-10-04 03:55:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32e55cec-f010-3a16-a810-d56cd4a96a5d | -19.5823 | -45.90354 | 2025-10-04 03:55:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eca057d8-3515-34c9-aa7d-0d1b72d00dbb | -17.1717 | -53.03954 | 2025-10-04 03:55:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 751a3dd6-a04a-3e90-a181-0573c7e450eb | -18.58761 | -43.46655 | 2025-10-04 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1bac3dfa-f06a-3674-af00-7b713d801d71 | -20.69685 | -42.07625 | 2025-10-04 03:55:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e913a34-9b68-3dfd-8b95-47143f4ef7e3 | -21.78406 | -45.33815 | 2025-10-04 03:55:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 154184aa-af9b-3235-a42a-ba573d76bd7b | -19.49747 | -43.62643 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d11afa71-a68c-3905-aa60-9191baa0e5fc | -19.58308 | -45.89946 | 2025-10-04 03:55:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e85ac35a-6525-3235-99be-2e90b573fd44 | -20.1378 | -46.42248 | 2025-10-04 03:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 400bd20e-db86-3910-b607-d6e81a823a67 | -19.61701 | -46.69688 | 2025-10-04 03:55:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88b4e460-2134-37f8-a036-42944698662b | -22.12574 | -42.91625 | 2025-10-04 03:55:00 | NPP-375D | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a55484f3-7c52-3909-8a6e-b0f861fd5f91 | -22.07868 | -43.10524 | 2025-10-04 03:55:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 16f9cbdf-984f-368a-9af3-9044ccae2028 | -20.94605 | -45.81455 | 2025-10-04 03:55:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd463ed2-2b0c-3f15-9fcd-b420c9d5ace2 | -19.73943 | -47.1924 | 2025-10-04 03:55:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a91cda6-ae0c-3ea7-92da-0cdf12ed60e4 | -18.23726 | -53.36757 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6be5d29b-5765-3489-b800-92efd68e43c3 | -20.10366 | -44.63596 | 2025-10-04 03:55:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee5e250a-02df-3fdb-ba5b-d5f135ad3612 | -19.7974 | -42.08384 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 081f8907-c928-302d-80a8-a090e90e1a8c | -20.13418 | -43.993 | 2025-10-04 03:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 722102fd-b4ba-38e1-aba7-150f322d0bb0 | -19.69388 | -47.96881 | 2025-10-04 03:55:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d72dc360-8aa3-3307-a4e9-bedaad877057 | -19.79856 | -42.08718 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 59bafa6a-c425-3907-8e9b-fc22d3929a89 | -19.77775 | -43.56203 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 039691a1-0b8c-3ce7-a356-f23775ae72b6 | -22.36807 | -47.0624 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 951aeff7-b0ed-3268-94ab-7bdb66c07cef | -22.36592 | -47.03836 | 2025-10-04 03:55:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8c8ad72-49ef-3226-815a-1f4e5bef7a25 | -19.00078 | -48.49433 | 2025-10-04 03:55:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a281da9c-5322-31c9-bb0c-499251288d7a | -18.2774 | -45.90928 | 2025-10-04 03:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32b647c2-a91a-3d4a-92f7-633fc90f6c50 | -21.93085 | -46.60627 | 2025-10-04 03:55:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5961d3ce-2a7c-321f-93e9-5a8e3a189735 | -19.96669 | -43.64365 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 995fab26-e3b2-332d-87d2-16cc996bea16 | -21.21506 | -45.82745 | 2025-10-04 03:55:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bbbeaf6f-c5d3-357b-9f87-6fea4b5b7eae | -22.27177 | -46.75603 | 2025-10-04 03:55:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 678a174a-732b-3ce0-bba6-f011df8761c7 | -21.34027 | -44.99829 | 2025-10-04 03:55:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 20ef2e5a-06c8-3de9-9254-7ffc691c65f5 | -18.59288 | -46.49639 | 2025-10-04 03:55:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43a8ae4a-50ba-38e6-a59c-28d1ecadbae9 | -19.76729 | -43.78973 | 2025-10-04 03:55:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71507c47-9f5d-3012-b7e8-a23ea601e492 | -21.19847 | -43.10957 | 2025-10-04 03:55:00 | NPP-375D | RIO POMBA | MINAS GERAIS | Brasil | 3155801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ab39e6dd-2b66-3fc1-b627-60f93b1d2075 | -19.96 | -42.31997 | 2025-10-04 03:55:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1260c5a9-3e45-3f2e-b37e-144e3cf1d9fd | -19.13705 | -43.14503 | 2025-10-04 03:55:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| feede407-4b41-3562-aeb4-adc710aa2267 | -18.54621 | -45.04491 | 2025-10-04 03:55:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df20d9b2-8ef1-3d83-9ce4-7dd205fb11f3 | -20.12685 | -43.99082 | 2025-10-04 03:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2f5144da-614f-3d81-8cee-42d684d7668c | -21.78897 | -45.33362 | 2025-10-04 03:55:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3406dbd8-1ca4-30e7-b7f4-e10b7019db79 | -21.35064 | -45.79761 | 2025-10-04 03:55:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6d515c4e-9795-3aa8-80da-b6489aeb7606 | -17.99165 | -51.63879 | 2025-10-04 03:55:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbde01f6-cc9a-3874-a3ba-8c1d46cba6fe | -19.97666 | -43.70666 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 35476ede-8e8c-3810-b8bf-6cb2e11b5212 | -21.52263 | -46.0782 | 2025-10-04 03:55:00 | NPP-375D | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| da1d0cf5-5b4a-37f2-947d-cb32858761f9 | -21.34142 | -44.99501 | 2025-10-04 03:55:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 45579301-8503-3992-bdd0-6c40ce4cf262 | -17.1702 | -53.04593 | 2025-10-04 03:55:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18bd94f0-d4a5-315d-aa54-8db8bbb99a71 | -19.74615 | -46.50405 | 2025-10-04 03:55:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0128e7fb-cd1c-3cab-8d4d-7688c2d117bd | -22.07518 | -43.10451 | 2025-10-04 03:55:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b49abc0-0a5c-359c-933c-65ba28f3652c | -21.60045 | -45.28893 | 2025-10-04 03:55:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0ee4d85a-2f53-360e-bc7c-cdb6f5020df7 | -20.47258 | -44.81709 | 2025-10-04 03:55:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cc50e8b8-192c-3d80-a2f5-1d2f588e22c1 | -18.27825 | -45.90489 | 2025-10-04 03:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b988255-bc30-303c-83ae-ce3f7097506e | -19.8611 | -42.58079 | 2025-10-04 03:55:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9ae6c2a8-02bc-327f-b268-0a4addd16206 | -19.7947 | -42.09984 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6988ae05-502c-39fb-b90d-a54ed75ceb8f | -19.97582 | -43.71133 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b806168-ec52-3c51-820a-a5b122419a25 | -19.94834 | -44.71434 | 2025-10-04 03:55:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92a179a7-c478-3357-bd0e-fa0356d4ec31 | -17.69999 | -47.09227 | 2025-10-04 03:55:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0e82a6db-3320-3bcd-b2f9-eea61d104e64 | -19.86957 | -43.65428 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c9a050b8-ceb8-3d5e-9ea6-c4ee70aa8fe5 | -19.45499 | -44.29115 | 2025-10-04 03:55:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5891ee3e-e56c-3bb7-95b0-a6287e611ebc | -20.41466 | -44.13554 | 2025-10-04 03:55:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5e8d0353-48db-3cee-a424-7dc3e51ba66c | -19.81565 | -46.07117 | 2025-10-04 03:55:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 648e183c-b0df-3c77-baa3-4eb5a737160c | -21.93589 | -46.60297 | 2025-10-04 03:55:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 285da7c4-f2e9-3e88-9e42-9d276e5876b7 | -19.73089 | -44.45396 | 2025-10-04 03:55:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8eab3c7a-acf8-3713-8df5-4c01ec2822f1 | -21.52339 | -46.07428 | 2025-10-04 03:55:00 | NPP-375D | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 66bd4670-0d98-31af-9f20-43bb194ba972 | -19.59668 | -43.8095 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa3d5d3a-820d-3ba6-989e-ff7327a848fb | -17.99512 | -48.3312 | 2025-10-04 03:55:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2c4d3f94-022c-370c-97eb-b9edabfdecd6 | -21.80534 | -45.64886 | 2025-10-04 03:55:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3623205b-5006-3726-9b54-c83c87488315 | -19.81483 | -46.07552 | 2025-10-04 03:55:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8597a22c-7910-36dc-b191-e21bb5883f20 | -19.71003 | -44.12758 | 2025-10-04 03:55:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12d2321d-44db-3e55-9ee6-ee9bc98abdd7 | -19.79192 | -42.09522 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f1a978b-7464-3ee6-ad60-c43ff8738e43 | -21.08868 | -47.76781 | 2025-10-04 03:55:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85d893a5-68c0-3878-abf6-c1928617d116 | -21.27723 | -45.05605 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 567a31a1-29d2-394d-a187-e9ae86f03843 | -19.71092 | -44.1227 | 2025-10-04 03:55:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 244e1163-22c2-3deb-a38e-56eb1baff44c | -21.17134 | -43.03505 | 2025-10-04 03:55:00 | NPP-375D | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8a05a4fb-2b81-305b-9461-7e79fbb84412 | -21.1921 | -45.14552 | 2025-10-04 03:55:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d15672cb-4f99-3c45-8c7f-06febbdf7288 | -19.24699 | -45.9953 | 2025-10-04 03:55:00 | NPP-375D | MATUTINA | MINAS GERAIS | Brasil | 3141207 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ece3acc1-b553-3c29-9a3b-cc7955977f0c | -19.13344 | -43.14422 | 2025-10-04 03:55:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 360b5bb0-5dd5-3434-8587-c87c2d07c731 | -19.79816 | -42.10048 | 2025-10-04 03:55:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb6c65df-d6cd-34ca-b7ed-5d60b74ac72e | -18.54958 | -45.04943 | 2025-10-04 03:55:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3060f3f-06ad-3ba8-b71e-e91ecc24dfc1 | -18.00017 | -48.33236 | 2025-10-04 03:55:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 404fec24-5770-3156-83f4-2407911699a0 | -19.52198 | -43.83806 | 2025-10-04 03:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b86b71c9-2619-3995-b310-2c272ac17345 | -18.17619 | -53.35005 | 2025-10-04 03:55:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7af163b6-84b4-32fd-87b7-0e99f961eb92 | -18.6302 | -50.67863 | 2025-10-04 03:55:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d37e6edf-de47-35a7-b98e-79c7b618cd46 | -18.63606 | -50.67951 | 2025-10-04 03:55:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30ca9d84-d2bc-36d4-8791-81f6e154060f | -19.96849 | -43.70959 | 2025-10-04 03:55:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 653a17d5-a688-347f-bef6-21875c53a1ac | -22.4897 | -44.07699 | 2025-10-04 03:55:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README49.md)
