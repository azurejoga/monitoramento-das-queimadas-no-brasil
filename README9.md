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
| 24f47e8f-6104-3347-ae4b-670967f281b0 | -3.316 | -48.7134 | 2025-09-08 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9a26fa1c-bc4c-3eb5-b3f0-486c356dc8f3 | -12.6341 | -56.9926 | 2025-09-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| b23c9e0f-761e-30fd-9f46-fb44f66c38ca | -10.71887 | -48.59449 | 2025-09-08 00:50:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ccb42bbc-11b5-38e8-a105-423bb1bc185c | -9.67569 | -51.06926 | 2025-09-08 00:50:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 566b91b0-ce8c-3b22-a453-f86ad00ba436 | -11.27459 | -46.46715 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ec46610f-bd56-3706-b9aa-e4af569399da | -11.22967 | -55.00934 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 481eb5da-1434-3ae2-a373-8d197868dc6d | -12.94805 | -54.79554 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 39f6f781-2ab7-3e0d-a040-ac8a384f1e2e | -12.8129 | -48.00014 | 2025-09-08 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c8f58e24-6bea-3ef2-879d-6affd9ca7616 | -12.20432 | -53.91453 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2dc4afe1-ef7b-380b-b48c-3a076f0211c4 | -11.21174 | -55.0227 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 05af0af7-8c0c-3fea-9ddb-d2946b66aae0 | -15.5374 | -56.32872 | 2025-09-08 00:50:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4456b10e-63db-37b9-8b7a-2d75d46fe6ae | -12.60938 | -56.98962 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f10afc54-10a1-3568-b6de-712f981a78cd | -11.40419 | -50.39142 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 729ee56b-14a4-3b92-84e9-32ff3e65956d | -11.20888 | -55.00101 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 25eecad5-b154-39f9-be7f-af59fe0108dd | -9.82449 | -53.31995 | 2025-09-08 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b7e81090-b760-3b9f-a671-61b8cc6b04c9 | -11.20065 | -55.0132 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a078dba8-6c66-31f4-8688-b33311f2cde2 | -9.85543 | -48.84326 | 2025-09-08 00:50:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1b1444af-73a4-3740-80f1-35102c18a13c | -12.93684 | -54.78572 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6a10efe3-83cf-3684-a66d-ce6e4d193adb | -16.43368 | -49.2827 | 2025-09-08 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5a5bda9c-3956-3355-a783-ee3f20afaa84 | -13.65079 | -43.81844 | 2025-09-08 00:50:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d771942a-d05f-30e6-95e6-b877ccd7496a | -18.58288 | -48.71842 | 2025-09-08 00:50:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7ec4c29e-ee26-380c-83b4-6dcbfdf677e6 | -17.26057 | -46.69337 | 2025-09-08 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 14fda84b-5433-3830-b02e-3865f574bdf5 | -18.96032 | -46.79146 | 2025-09-08 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e9e30319-070d-3751-bd42-aa27896b5f93 | -11.63559 | -49.02777 | 2025-09-08 00:50:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0f061315-7ccc-3ba7-b720-cbc6ffca9516 | -11.38087 | -50.42488 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| b0b192c3-0b4a-3404-ba36-e773a62f6026 | -15.38095 | -53.94795 | 2025-09-08 00:50:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cc68d08b-3109-3169-a241-f8c103a53b53 | -9.82327 | -53.31098 | 2025-09-08 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae97f67e-84fc-37a6-917e-caa4d1dae083 | -14.87913 | -55.7999 | 2025-09-08 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 26ec5d03-25ab-35de-b2e7-94eea9dcddab | -14.51942 | -48.76911 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2a4224a8-8e09-3806-ab38-21c29824a278 | -11.60483 | -52.19495 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9b5417e5-dc33-35c8-823c-2410a581e566 | -14.52108 | -48.77997 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 491ce7ba-d670-31a2-ae66-78067b4b0b23 | -13.8974 | -53.99166 | 2025-09-08 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fe6237ed-3f5f-36e7-804b-71a047df8181 | -10.81474 | -47.73375 | 2025-09-08 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 621a271d-a457-3363-95e1-8833eb96586d | -16.90085 | -45.76439 | 2025-09-08 00:50:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1449ea63-9e03-3707-a413-f1f8d7b88168 | -10.4647 | -53.63163 | 2025-09-08 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c3daede3-46d6-37ea-886a-98f844e8b00f | -14.7213 | -55.91741 | 2025-09-08 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4b47f701-fa16-3ca9-918d-89e59b9e2874 | -15.29238 | -43.39252 | 2025-09-08 00:50:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 94435a6d-3267-37e6-b76b-f9a87217e317 | -16.33863 | -45.04247 | 2025-09-08 00:50:00 | TERRA_M-M | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c2dcc98f-bd8e-3481-8efe-6a68ceada95f | -10.00339 | -51.62626 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 955bc0ae-1aa9-3a6b-ad5b-0608adfea216 | -12.6303 | -56.97127 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 443.7 |
| bc88d8e9-23be-30a7-8fe1-09f69619d2fb | -11.59601 | -52.19624 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 597e8aa2-98ba-30af-852b-f38e8154feb2 | -16.34505 | -52.951 | 2025-09-08 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3f4ef8a4-3a43-3fb2-8715-f889520634a8 | -14.50089 | -48.79998 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 265279fe-d59b-3dbc-bce1-803ad28916b2 | -13.82191 | -43.85667 | 2025-09-08 00:50:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9898ef3a-dc5d-357a-bf0e-7043e2bea68e | -15.84672 | -52.3097 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 40e3af46-dfbe-3e8d-89b5-c9a1ac03f7de | -11.66212 | -46.89138 | 2025-09-08 00:50:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0b58564a-09fd-3eaf-9c87-7471a083b043 | -17.7058 | -48.70678 | 2025-09-08 00:50:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a145eaee-2546-3e67-9b9b-6cc2ed3ce375 | -10.79277 | -47.7372 | 2025-09-08 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 30a09f05-79e2-3a27-b8ce-8b9d844b97b9 | -15.29552 | -43.38626 | 2025-09-08 00:50:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 50.6 |
| 16603b47-033d-3aba-b1ed-0bfc595973bf | -9.56604 | -53.59401 | 2025-09-08 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 84ada256-17bc-3a7a-bfa1-1b38c088b6a6 | -10.00467 | -51.63534 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 08394638-81d4-3228-9bc8-46d87095a47e | -15.66972 | -48.24967 | 2025-09-08 00:50:00 | TERRA_M-M | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d536a04c-2a6f-3ecf-81af-2a497c40ca25 | -18.13901 | -48.51793 | 2025-09-08 00:50:00 | TERRA_M-M | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4741257f-5cf5-30a7-885a-b1d1f2862da5 | -15.25329 | -53.81992 | 2025-09-08 00:50:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b4cd07f7-1d9d-3eaa-af65-efdc71022071 | -18.0272 | -47.11604 | 2025-09-08 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 7a0ffb8b-12e8-3952-a3c2-96e9c3005c3b | -9.95115 | -51.19228 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 35fdf1a5-ebee-3d01-ba35-1d5fc5d5e6e9 | -14.80724 | -48.17603 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f5df450-8109-3dea-a821-c425d7f1074d | -11.37521 | -50.38587 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 91252fc1-fa45-33cf-bd99-2dd1042ef37d | -8.74637 | -46.67776 | 2025-09-08 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 11629bee-622f-37f9-8d7a-aff44aa53ffa | -12.95801 | -54.77711 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7034ce77-7089-3082-85b7-1e9545c0db98 | -13.2772 | -51.77506 | 2025-09-08 00:50:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91eec998-7307-31ed-a3de-302981a57d52 | -14.29293 | -44.87449 | 2025-09-08 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 9be8e894-6c78-3d79-a6b5-1f93fe0ec4f7 | -10.00595 | -51.64439 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a8e66691-e0e0-3490-99c6-58d29cb6632b | -15.18505 | -47.96647 | 2025-09-08 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dabb25c5-32d7-30f6-9c48-d883bbf5413a | -18.12381 | -46.82514 | 2025-09-08 00:50:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c5de6f95-48de-3930-a3b4-3b2ae851dab6 | -12.17149 | -43.95033 | 2025-09-08 00:50:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7f44e9d2-c9d6-3f1a-8b11-68f967093f7c | -15.71688 | -53.5545 | 2025-09-08 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9c39ee38-9c8e-39c8-8ac9-51dc01db6db7 | -15.24623 | -52.36312 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cce364b6-69bb-38be-aef4-ad3cf76bc50a | -11.8494 | -51.0542 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| de99f83f-1a6a-30b0-ad53-8ef2b5a05ccb | -11.34764 | -50.39009 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 21808a5c-4ae4-3e18-a7c5-a1efdff0e1e6 | -16.35296 | -52.93986 | 2025-09-08 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e4b7d2f9-31e1-34a4-bd70-c3eba06a2320 | -15.23605 | -52.35518 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f0696171-2808-3a2b-aa76-2e368db5e941 | -13.00857 | -45.2209 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 37823b73-495c-312d-ba56-5ddbf97eca90 | -14.79636 | -48.10608 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 86dd6f90-8cf6-3f8c-b7b0-f3927d0a32b8 | -11.37663 | -50.39564 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a1faff3f-8e4b-37ea-a39f-90981378c323 | -13.0382 | -47.13758 | 2025-09-08 00:50:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 30c5f590-dcaf-3d26-95ab-2f05197d34bf | -12.82116 | -52.94417 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 23208b98-8862-3d08-87f7-bdb9258ce034 | -17.15663 | -44.43291 | 2025-09-08 00:50:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 102.0 |
| dd489ae3-a919-35e5-89d3-4c1939532e2c | -16.44784 | -48.03854 | 2025-09-08 00:50:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7d68dcfa-a6ca-35c6-a82d-0884861ae24a | -17.44758 | -50.2291 | 2025-09-08 00:50:00 | TERRA_M-M | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3dfce6f9-83bf-32d5-b8bc-6bece8797513 | -17.15984 | -44.45127 | 2025-09-08 00:50:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 41412e0a-8070-3733-a97d-490fb3b6e48d | -13.35177 | -44.43031 | 2025-09-08 00:50:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 79ccad89-fd92-3c12-aa08-7e4d26ffe053 | -16.43516 | -49.29258 | 2025-09-08 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 621f8e8b-a09d-3539-9bd0-afdf7285c67e | -13.72702 | -46.89886 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ff453929-9684-37f3-8a39-4237c450a2a0 | -15.76192 | -53.56316 | 2025-09-08 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1ad6887d-a493-3eee-8a85-98c1ca4d5377 | -11.62865 | -52.23713 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 80420353-b75c-354f-93fa-a3b57947dd43 | -14.50249 | -48.81074 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 93811f7c-af2e-3e03-b31a-96a9f11b6bbf | -12.94658 | -54.78436 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b7b96d8d-92c1-3779-ad12-6276e7e7c2d1 | -10.51254 | -57.80547 | 2025-09-08 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 55a015da-f2a8-3b31-8f75-3005d8c323b1 | -12.93975 | -54.80807 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 68c5075f-f740-31be-a217-2394be14e759 | -9.67702 | -51.07862 | 2025-09-08 00:50:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c4bbe2c8-021a-3a9f-b4ae-7fa69b27dae5 | -11.42872 | -43.64464 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9bf99a00-ba16-3e28-995b-be384f910d51 | -11.6131 | -47.16204 | 2025-09-08 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 161bbd7e-46ad-34ec-aee8-57220f181460 | -12.83407 | -52.9046 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 82f2ab36-83b1-37a2-b0c5-9829f521f5cb | -11.63747 | -52.23584 | 2025-09-08 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 44cfe307-bc91-3b1e-b0e5-fa5aec0dd426 | -15.16861 | -47.99315 | 2025-09-08 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1aa4e602-169f-38b5-8e64-dc9304bf330c | -11.37946 | -50.41514 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 0ac95d82-cab7-3c7f-8d5f-cc61c5665ab7 | -14.71047 | -55.91883 | 2025-09-08 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 221a9d60-8816-3d71-b1cd-6d8aa4c2cc8a | -15.83531 | -52.29845 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a526159a-cb7c-36b1-9dc7-5c721e1bb121 | -13.5465 | -48.1109 | 2025-09-08 00:50:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README10.md)
