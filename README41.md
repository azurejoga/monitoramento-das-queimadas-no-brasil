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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46b6330b-c1f5-3149-a438-f6cd980ad7ff | -9.17888 | -44.72009 | 2024-11-28 04:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5196c85d-0533-3c09-a3ee-508596b97564 | -21.12442 | -47.85795 | 2024-11-28 04:04:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 941e5fad-1a20-3600-a250-403dca5361f8 | -20.6743 | -49.12072 | 2024-11-28 04:04:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 240cbc9c-77fa-390f-b8d0-099a5889c111 | -20.457 | -46.14528 | 2024-11-28 04:04:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cae88316-9247-33bd-86ae-687e1ebc46d9 | -17.85054 | -46.00396 | 2024-11-28 04:04:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7392a3f-ac30-38fc-98c5-492e1789ead4 | -22.01011 | -41.26761 | 2024-11-28 04:04:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0fcd0e6-b59d-31d5-8f5c-a6f3c2305322 | -17.74352 | -44.52968 | 2024-11-28 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a22c3643-db8a-329b-b043-7630f8ac06b0 | -18.68908 | -48.97514 | 2024-11-28 04:04:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 952cab1b-b65e-351d-a60f-83e418972ab1 | -21.11919 | -48.64824 | 2024-11-28 04:04:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4eb26170-dc62-3f84-996c-bea2cc46137c | -21.19463 | -44.93886 | 2024-11-28 04:04:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a3a71ed-e979-36ac-bb42-e3c6a73c906a | -18.77505 | -55.84056 | 2024-11-28 04:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d673d2aa-a0bb-309d-9f4a-807bedbe8e0e | -17.171 | -44.87584 | 2024-11-28 04:04:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e081c6ce-2fd4-3df5-b8e4-f333cceb110e | -22.05548 | -49.73769 | 2024-11-28 04:04:00 | NPP-375D | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 46638a8d-2060-39ea-a3da-6b716de96963 | -20.31156 | -45.58388 | 2024-11-28 04:04:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e730d3f-9fcb-30ad-8092-654809e07534 | -19.20778 | -45.37735 | 2024-11-28 04:04:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13c2ab26-b79e-30d1-a6da-1fe9d341f14d | -20.80013 | -45.89819 | 2024-11-28 04:04:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41f63d2e-5425-30dc-8716-196da42e4d76 | -19.52367 | -47.3296 | 2024-11-28 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d7d2f7a-23d0-3389-b683-0556da7d0dcb | -16.90941 | -48.28974 | 2024-11-28 04:04:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 103d04bb-9b03-3e03-a0ce-870ce19271c0 | -20.35274 | -47.45412 | 2024-11-28 04:04:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8149666b-0fa1-3af5-a948-7ac2c59d2433 | -17.09659 | -44.97523 | 2024-11-28 04:04:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bb6f460-7b8a-3e1c-b0f8-a468613bd13f | -22.11576 | -49.60809 | 2024-11-28 04:04:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87639364-f6a4-3e1c-bf44-726d73a36ae2 | -19.33094 | -45.62818 | 2024-11-28 04:04:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea227732-6287-3d74-8995-68684754e441 | -20.12659 | -53.32272 | 2024-11-28 04:04:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4816debd-5880-370b-9293-5c7ad96b2a9e | -19.52262 | -47.32759 | 2024-11-28 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd8cad9f-e947-36ed-ad9e-c3c82dc54c72 | -18.76859 | -55.83887 | 2024-11-28 04:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8fbfe5e6-8b84-3397-9268-4bac943f172e | -21.18001 | -43.9798 | 2024-11-28 04:04:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 02af8f22-a651-353e-9911-fc0c1cc89f7c | -20.72389 | -54.43532 | 2024-11-28 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dec6f89f-570e-3a76-85bc-71226f9539af | -20.44305 | -42.36058 | 2024-11-28 04:04:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8d4e887d-d5e0-3cdb-b3da-c5dda3545480 | -20.42563 | -48.78024 | 2024-11-28 04:04:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 861cb75c-3a7d-3dc6-96fb-cca8060eeb09 | -21.62641 | -43.46644 | 2024-11-28 04:04:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be441dcb-f87e-364f-9a44-548b3cb84e22 | -21.12536 | -47.85282 | 2024-11-28 04:04:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acacbd93-d1b2-3876-aa6b-2081cc3d322f | -17.62486 | -42.61131 | 2024-11-28 04:04:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8bb8f251-1bfe-3ff5-a1a1-f9db7f484765 | -22.60809 | -46.1978 | 2024-11-28 04:04:00 | NPP-375D | SENADOR AMARAL | MINAS GERAIS | Brasil | 3165578 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ed2e4645-d8b8-374d-8e3a-ead43611101c | -20.90022 | -43.81868 | 2024-11-28 04:04:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9b5da06e-1efa-3de9-9686-e2e443b61266 | -19.52655 | -47.33545 | 2024-11-28 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66608aca-2328-3efd-b709-48bd9c548c5b | -22.32124 | -46.32699 | 2024-11-28 04:04:00 | NPP-375D | INCONFIDENTES | MINAS GERAIS | Brasil | 3130606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8ce8d41-0d6d-361d-b636-0412389124bf | -17.98824 | -43.42998 | 2024-11-28 04:04:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| acc6bba9-7921-3987-9147-84f31cf34915 | -17.99158 | -43.43058 | 2024-11-28 04:04:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a8545eab-5c51-326a-a8f7-1ecbda657f81 | -21.49881 | -45.10667 | 2024-11-28 04:04:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51553bf1-8df5-3852-a8b9-7fd7d043d2d9 | -23.36979 | -47.06222 | 2024-11-28 04:04:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| fd765f52-f017-30ea-b29f-9e0b5aea876a | -22.85712 | -42.97952 | 2024-11-28 04:04:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d72618c4-3554-37d0-93cf-101534e7c073 | -20.3282 | -48.82027 | 2024-11-28 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a16c617f-55ce-3277-884e-d16af042de3d | -21.1317 | -49.98637 | 2024-11-28 04:04:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 52fd6881-751c-33f1-9531-5852e5b67316 | -16.67999 | -43.88498 | 2024-11-28 04:04:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f7ee016-807e-3f4c-a050-628dcb2327a4 | -17.28827 | -44.35042 | 2024-11-28 04:04:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b89062a8-a142-3ffd-bc0e-f6255b0c0b38 | -23.37133 | -47.06055 | 2024-11-28 04:04:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 61ef25ad-fa1c-3bea-b512-e43b37e53998 | -22.69961 | -43.34748 | 2024-11-28 04:04:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 154a6ed5-8672-35ef-abab-3db5ae5c206d | -20.72762 | -45.17948 | 2024-11-28 04:04:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6953ed74-e5f8-3549-a670-bd869156fad4 | -19.54189 | -47.33831 | 2024-11-28 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06e5f67e-0979-3b3f-bc6c-3e338ba54ff1 | -22.0597 | -49.73862 | 2024-11-28 04:04:00 | NPP-375D | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| efd6d17f-135e-39c2-98ec-5eab93345cd2 | -23.33457 | -47.65835 | 2024-11-28 04:04:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c0038b1a-776a-3d00-8561-d9fa9bdf3a71 | -19.30306 | -45.53726 | 2024-11-28 04:04:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4a4a972-7537-3119-ab9d-09dd67a04440 | -21.82836 | -44.19191 | 2024-11-28 04:04:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d196fe8-e447-3cf7-9ecd-c996fa5f27ae | -21.12428 | -48.64482 | 2024-11-28 04:04:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a04f70db-64ba-3348-8a40-35c79ca229cd | -17.17031 | -44.87988 | 2024-11-28 04:04:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7918395c-94bb-3a31-933f-9cf8f97c9072 | -23.40733 | -46.55542 | 2024-11-28 04:04:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3b12979c-5881-34c5-b35f-477bae0e8cc0 | -21.12321 | -48.64909 | 2024-11-28 04:04:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 13787ae6-52a6-3b47-85a2-ba6d32a316ba | -19.52553 | -47.33346 | 2024-11-28 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c11ab1a-fb63-3847-9a41-d75d8146e2b0 | -17.37821 | -42.48399 | 2024-11-28 04:04:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8f75f7f-36b3-39af-aa8d-ece63b9b7270 | -19.33165 | -45.62404 | 2024-11-28 04:04:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38ef2065-fefd-3524-a973-a3b7cb32d089 | -17.67571 | -42.74287 | 2024-11-28 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed6c39ee-2bf6-39c7-a779-a09753f64079 | -21.1686 | -48.69755 | 2024-11-28 04:04:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2a93022-f969-34e0-8031-746af7929332 | -16.34726 | -43.69656 | 2024-11-28 04:04:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 483f0252-4448-3013-a206-1f085c2cd752 | -22.11652 | -49.60416 | 2024-11-28 04:04:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 516e9b06-d1dc-38c0-bc57-f69743b9c771 | -23.47777 | -45.34605 | 2024-11-28 04:04:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e88ce5a2-a137-3b01-8fa9-6cd3158c077d | -18.25504 | -51.26812 | 2024-11-28 04:04:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c7e2a62-577e-3f59-99c2-bbb0632025cf | -23.36698 | -47.05714 | 2024-11-28 04:04:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 235ca025-2389-3a27-8fe8-7e4d9b39fa16 | -22.90539 | -43.65736 | 2024-11-28 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a7bbab1d-97e4-3a85-986b-b6b80c179fd6 | -18.78151 | -55.84227 | 2024-11-28 04:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 79fee4d8-ce14-3f3a-a4ed-30afc27c1d5c | -22.58751 | -48.04746 | 2024-11-28 04:04:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aa1e235-724e-3467-9bd6-27e44c028b79 | -21.12391 | -48.64533 | 2024-11-28 04:04:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 436ccc22-5990-37d6-9d5c-51124d19d761 | -21.12356 | -48.64856 | 2024-11-28 04:04:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35300856-5873-30cb-a351-c4b4bd7e8376 | -22.90206 | -43.65675 | 2024-11-28 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f7523ca3-cbd8-3ae1-bd41-6f92dec411f9 | -20.33094 | -48.82119 | 2024-11-28 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d77ce483-ca0e-3e06-b774-a948894c0b24 | -22.12071 | -49.60505 | 2024-11-28 04:04:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a93d5c29-0e23-3f5a-a8f5-156053d6955a | -21.82897 | -44.18816 | 2024-11-28 04:04:00 | NPP-375D | ARANTINA | MINAS GERAIS | Brasil | 3103603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eaafcd6b-451d-3a66-b6f2-9bb26d701953 | -21.62559 | -46.37707 | 2024-11-28 04:04:00 | NPP-375D | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0b0c091-e2a5-3539-a412-d9c380da97b2 | -19.52274 | -47.33461 | 2024-11-28 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8971be0f-6e8f-3c15-9b36-30970877a540 | -22.82516 | -46.32315 | 2024-11-28 04:04:00 | NPP-375D | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1851ae57-240f-389d-89de-a17e6952c215 | -22.46554 | -47.13556 | 2024-11-28 04:04:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e7f11eee-1615-32d7-b714-2a12bdc18503 | -20.32683 | -48.82025 | 2024-11-28 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0d4e00c-adb1-3e49-825a-f64f39918974 | -21.16932 | -48.69376 | 2024-11-28 04:04:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcf2a015-1681-37b1-800d-d136e395018a | -20.76271 | -46.76841 | 2024-11-28 04:04:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4cdae7ae-fbca-3b06-871d-7290ee73284b | -17.29171 | -44.35104 | 2024-11-28 04:04:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7578768-1e50-3ad8-911b-4565ef785259 | -20.71815 | -54.43379 | 2024-11-28 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eba9dfd5-ff22-3980-a334-fd68ff02ace9 | -21.49832 | -48.61247 | 2024-11-28 04:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4260535-17f5-3ba7-bf6b-2956888dabb9 | -16.92201 | -43.60643 | 2024-11-28 04:04:00 | NPP-375D | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa5dbb14-6be8-300f-a62d-710570b6dcf3 | -21.5023 | -48.61337 | 2024-11-28 04:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b8f377-6c25-39cd-9a36-a91a1575e396 | -20.7191 | -54.42959 | 2024-11-28 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d5fea750-7cad-3b31-abaa-3a74f2aa0fec | -18.78017 | -55.84803 | 2024-11-28 04:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7af279e8-f120-359a-b14c-1bb4f087a888 | -22.66911 | -47.08579 | 2024-11-28 04:04:00 | NPP-375D | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dfa579c-694d-383f-9cc4-bc303f0034aa | -19.51425 | -44.27667 | 2024-11-28 04:04:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33e9c283-62e7-3d0d-83e7-31138c2a1c3d | -20.5805 | -44.57415 | 2024-11-28 04:04:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6d0a89f-5463-3404-9bff-aa1bc5fbaa7d | -18.7737 | -55.84633 | 2024-11-28 04:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 86147091-2159-34ac-916b-5d4ae07586be | -17.94938 | -47.07222 | 2024-11-28 04:04:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07795794-f5f0-3f31-afd9-0cebc5938b27 | -22.90063 | -43.75302 | 2024-11-28 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2dc73fd6-4411-3693-a4b4-27bd6bc4cc8f | -21.89557 | -46.50559 | 2024-11-28 04:04:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 377cf950-9f0b-30a8-a15d-b3a01e9d4d8b | -19.30657 | -45.53794 | 2024-11-28 04:04:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27529552-8241-3d13-a9dc-1e4fef1e6f2b | -20.30106 | -41.64207 | 2024-11-28 04:04:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 9ff35130-7194-35de-be50-22291e2262fb | -17.85132 | -45.99951 | 2024-11-28 04:04:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README42.md)
