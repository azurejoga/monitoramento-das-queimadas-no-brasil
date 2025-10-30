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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3a776de-1aa4-349b-a5e1-08c5deb8f0ce | -14.76487 | -44.9682 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a75845b9-fa5b-38a9-9a59-b57879e154f5 | -14.48062 | -51.52757 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c8170d9-18aa-3416-8f81-a21e093a69d8 | -19.06336 | -41.12943 | 2025-10-30 04:08:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 289daaf9-30de-3e29-9904-33eb66b7b5ed | -16.88783 | -41.99967 | 2025-10-30 04:08:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4c5412af-92fd-3f51-b8d2-4e6f6b82adaa | -15.02215 | -46.32492 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e9f54a52-3b83-3af7-9c65-19245aec7a47 | -15.55824 | -42.97964 | 2025-10-30 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd8ac7cc-820c-3009-a70a-3694e26b75d4 | -16.06405 | -42.31326 | 2025-10-30 04:08:00 | NPP-375D | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2682a71-61a6-3cb0-803f-15e67b56ac78 | -16.62515 | -40.98483 | 2025-10-30 04:08:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5da943c9-0d42-3306-9b2a-c0b7e773c96f | -18.12839 | -42.60867 | 2025-10-30 04:08:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cc88225-47a4-3357-964f-ef19adb3d301 | -16.58967 | -43.51381 | 2025-10-30 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aa71a29-effa-372f-a077-64795c52a4da | -18.53927 | -41.58421 | 2025-10-30 04:08:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 040ac170-f12b-359d-b860-9b9afdb2d432 | -17.96214 | -44.07819 | 2025-10-30 04:08:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4abcc909-103c-3505-bed0-7b6121a2f84a | -16.74251 | -41.69699 | 2025-10-30 04:08:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ebc01e21-183c-3da9-a927-301a7fc8312f | -18.04906 | -43.15108 | 2025-10-30 04:08:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 708c5dc1-9d40-34ec-b901-b05af7920b02 | -15.01828 | -46.31746 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aaf1921-89a7-37dc-8c8c-7df739b61164 | -19.77401 | -42.41994 | 2025-10-30 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0353b872-0948-32fe-aba7-dc4c5150dab1 | -15.14382 | -41.58764 | 2025-10-30 04:08:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ea423a2-ab62-3eb4-be07-93626a36dcae | -18.5477 | -41.57414 | 2025-10-30 04:08:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cced06f0-2b48-370d-89a4-524a5b943606 | -15.32232 | -42.99212 | 2025-10-30 04:08:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e19e2823-f4cb-3a2f-b22f-7b25ffdaed19 | -14.77347 | -44.98278 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ead1e323-5d29-3bc3-b237-26b4fc26a1b1 | -15.38788 | -44.36636 | 2025-10-30 04:08:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e516a08-fdb7-30a7-b26b-c744b5f38f88 | -19.47005 | -41.5554 | 2025-10-30 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 57c15c39-7fc8-3dad-a3bc-9d96b834a498 | -14.48651 | -51.50217 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1b8fe8d-e033-3e76-af4a-bd5ae2478ed6 | -19.33852 | -43.06221 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 686d8025-3708-3c50-a738-35c1739e1af8 | -14.76129 | -44.96755 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dc63e79-209e-3ed9-8ef7-09e9832dda01 | -15.02375 | -46.30881 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ad4edc0-04df-3e26-b7e9-c69654313b45 | -17.95145 | -42.99987 | 2025-10-30 04:08:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35c5a04a-1b94-3dfc-b1fa-87f343e54d9f | -19.33462 | -43.06529 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 27941542-c576-377f-bf16-4b386498796d | -15.6135 | -43.98637 | 2025-10-30 04:08:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66fa3008-2891-304d-a6fd-dc14cd0a3db1 | -17.14503 | -41.93448 | 2025-10-30 04:08:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0a8eaff5-f96a-31a5-afa3-bd32e7ff8599 | -19.33072 | -43.06837 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eac6f061-1c37-3ca4-8b56-a3d9d1d76bea | -16.04943 | -41.47251 | 2025-10-30 04:08:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 57c07949-4a29-3762-afd1-b9f360391d29 | -15.01992 | -46.30806 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad31684c-9d56-3330-8f65-11989f46d4e3 | -14.97467 | -43.38588 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 662a8982-efe4-37be-b141-ff3420e1af50 | -17.14447 | -41.93811 | 2025-10-30 04:08:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0097fd69-f3e2-3c02-aa8d-6d14386205c9 | -14.7198 | -45.10025 | 2025-10-30 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d73adef-60bf-3457-b5eb-fa1f4a0c6d0b | -19.43097 | -43.05552 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 15f83463-18c7-3433-b700-a11656e6fc9d | -19.33404 | -43.06895 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2940fb64-7c1d-3f57-82dc-b43a6fff4e39 | -16.05069 | -43.71178 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 088decaf-9333-378c-9657-0d798126456d | -16.30373 | -43.8092 | 2025-10-30 04:08:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76815a5a-9161-3504-96d5-24cc7adab204 | -15.0654 | -41.97808 | 2025-10-30 04:08:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 834658c8-bdd0-36b2-b9e7-e805d2a5934b | -21.40099 | -41.9431 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1c3d521-246d-3861-aa3d-b2c1be0466c5 | -20.53312 | -45.76756 | 2025-10-30 04:08:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a06e1d5-5d55-334f-9c59-fb2758897213 | -15.09472 | -41.98664 | 2025-10-30 04:08:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a2cd822e-901a-3cc4-bc4b-a652f418ed55 | -17.01819 | -41.85794 | 2025-10-30 04:08:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 57dfe5f9-723a-3b8a-866f-b9532872a393 | -17.10996 | -43.49339 | 2025-10-30 04:08:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1f074ca-3cbc-3bc9-8a89-70f3d456e2f5 | -14.48578 | -51.50571 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0af5f249-0c65-3020-a964-600be0084c8d | -20.31685 | -42.06577 | 2025-10-30 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4588923b-9fc4-3c11-9aba-13bc4943ecca | -16.68226 | -41.3656 | 2025-10-30 04:08:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0e8c0f61-02bc-3e03-a649-e91d5cf7109c | -13.93508 | -48.4859 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ea50384-bcd3-338e-a5b4-fe013f10df31 | -15.94456 | -45.21724 | 2025-10-30 04:08:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93dbf18d-b473-3706-b8f8-444318499bc1 | -14.33861 | -46.89023 | 2025-10-30 04:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a340037-449e-321e-8c34-779ba1877e38 | -19.89173 | -42.63638 | 2025-10-30 04:08:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f5b3ca08-0f96-37cc-bd01-afb7728b9b51 | -18.21719 | -46.6288 | 2025-10-30 04:08:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4764b923-4a69-31de-b0b6-c3efa5f6ea67 | -18.57728 | -43.08533 | 2025-10-30 04:08:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 644d579f-0239-3d95-b8ab-73732ebe01d5 | -14.75556 | -44.95783 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a980ae57-079d-3926-acd4-10955aedf6a8 | -16.6817 | -41.36924 | 2025-10-30 04:08:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 94db6dd7-0915-3de4-9178-743bbce53102 | -18.23616 | -42.37343 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9d9c99c0-291a-31c9-bf9b-fef6a0e78448 | -13.94104 | -48.45381 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca33914a-4971-31a1-9ab9-2a5aae6ce853 | -19.34951 | -43.07918 | 2025-10-30 04:08:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| de8bd3a3-38b1-3d0b-bbe8-88d237f12d74 | -15.85498 | -44.89405 | 2025-10-30 04:08:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28c8f7ac-f757-3394-ae7a-d99f08bd8435 | -14.97028 | -41.93683 | 2025-10-30 04:08:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 1ff337b0-3207-3d06-8bfa-cfb9823a5ddb | -14.48551 | -51.50271 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e68891a3-b3f2-3373-a7d0-43d788eea272 | -15.55489 | -42.97906 | 2025-10-30 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 564598a2-d4ad-3745-b530-5acbf6171d2a | -14.77706 | -44.98344 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5b40e53-6f78-3920-8532-96518b402c67 | -16.82684 | -43.1097 | 2025-10-30 04:08:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a04ec12f-9640-3e85-ad1d-d4487500ba99 | -13.93422 | -48.49052 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0eb2973b-1f9a-35c8-bac9-85f2cde4a8e7 | -18.04574 | -43.15051 | 2025-10-30 04:08:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9bbf3b40-b4b6-3eb6-a0c6-45292b9d2350 | -15.28205 | -44.10834 | 2025-10-30 04:08:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c72a6de7-7cd5-36e3-9c9e-01b1dd5b5d83 | -18.23226 | -42.37651 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c41d7ca2-b579-3ca4-ac3a-9b72d183a5b6 | -15.79883 | -43.83812 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74931b72-0481-316f-ac0f-cf2765a8c6e2 | -15.83608 | -44.36623 | 2025-10-30 04:08:00 | NPP-375D | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30313ee8-ca5b-3128-b7c4-28ec837d2a54 | -14.97406 | -43.38959 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0c6171b-c996-3a97-bf33-8264d7a7bfdc | -20.32022 | -42.06637 | 2025-10-30 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c30c5fd-9372-3824-b3d5-0c5493f9c8cc | -18.22893 | -42.37595 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee2589bb-11d6-340a-ae21-725e5c70687c | -19.33578 | -43.05797 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ad60ce17-e931-3b11-8dd7-e82ec1b7d8c8 | -14.77993 | -44.98832 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 342fba5c-1f86-33f3-ad84-3e1436103d0c | -16.13081 | -40.26017 | 2025-10-30 04:08:00 | NPP-375D | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b97b3b9-08ea-3a9e-b08d-17284aeb5f04 | -15.2724 | -43.06588 | 2025-10-30 04:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6518fa1-7199-30ba-8f9e-e6ba3e38a4cd | -14.48272 | -51.51689 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e80b1c6e-e359-3bd7-a2c8-615930bb2150 | -18.04052 | -42.08587 | 2025-10-30 04:08:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b345c45-7801-3081-b991-ce6cb3f05b81 | -15.83954 | -44.36687 | 2025-10-30 04:08:00 | NPP-375D | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1327a6ae-f6ad-3c61-bf5a-fc2983c8b611 | -19.67791 | -41.98053 | 2025-10-30 04:08:00 | NPP-375D | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3946fdeb-5f4a-3f4a-8d04-fa3d04792852 | -16.03742 | -43.72869 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d80d0223-5604-39f6-a3a7-66963f9afc4a | -14.77634 | -44.98766 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fff8cec7-6c53-3fe6-afb4-1217919dfe71 | -13.93578 | -48.45721 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c50351fc-962e-3e34-bf47-1e0db5408886 | -16.58994 | -43.51705 | 2025-10-30 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 826155d2-f3c6-3af8-b3a9-623f58a322b8 | -15.02683 | -46.32098 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f00dbb53-f8e2-30d9-939d-1e6779ae1525 | -19.35283 | -43.07977 | 2025-10-30 04:08:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b22abf7-aa84-31e7-b64f-60acb7c4e7fa | -15.02596 | -46.32579 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdbef391-2b30-3588-9be2-818482c32264 | -15.58603 | -43.15613 | 2025-10-30 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b6a2d57e-8f92-3a96-b068-0d13ff50164d | -18.5505 | -41.57846 | 2025-10-30 04:08:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 68389cf7-d754-384a-9d21-b9f1c966c8a5 | -14.55218 | -49.25977 | 2025-10-30 04:08:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ed99ba3-42eb-3b86-ac9a-e8ecee67d08a | -16.59392 | -43.51392 | 2025-10-30 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8ccde7e-e5f6-303b-aec6-a2b4e23c4246 | -18.04632 | -43.14687 | 2025-10-30 04:08:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 31dc79cf-9e7e-31d3-be9f-3406fad226b1 | -17.708 | -41.15182 | 2025-10-30 04:08:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a71eeb58-04d5-3aa2-b929-7349ff133b6b | -20.40014 | -41.53051 | 2025-10-30 04:08:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 73d4952f-f503-3142-b467-1b8de9201c19 | -15.02303 | -46.32009 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a65203da-a66e-34a6-ac5a-e21c697b8376 | -18.23283 | -42.37286 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ddd5b6c8-f5f1-3f85-8c58-954b380f4fe8 | -16.6291 | -40.98168 | 2025-10-30 04:08:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README37.md)
