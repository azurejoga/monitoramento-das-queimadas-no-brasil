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
| b6f80460-51bc-31f1-ae6b-3a55f4b15dbb | -6.76137 | -46.30809 | 2026-06-25 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4b49d72-b46c-3f5b-bd21-717a99ef4ce8 | -10.39741 | -56.76639 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b1f7931-51f8-3844-9fc4-9789ea363305 | -7.75217 | -44.61869 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2db29431-c843-309d-b71f-c1b20202d8ca | -8.06315 | -46.38891 | 2026-06-25 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c56e383-cdf0-3cd2-8e5a-4a23b44946c0 | -8.7948 | -44.8118 | 2026-06-25 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36de72e9-34b9-30bd-90bd-09bdc11f2ccb | -10.39708 | -56.76356 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1815b10-9f99-384f-a504-82031d8e614e | -9.74008 | -47.87699 | 2026-06-25 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dab9442-e8c4-3cda-959d-226d10b73786 | -11.57871 | -54.71392 | 2026-06-25 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ed7ad66-c854-39c6-ac49-a06ff4e7f48d | -11.61966 | -48.49133 | 2026-06-25 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be86ffca-fac3-391e-8fcf-424aa5b73b44 | -10.52878 | -48.16019 | 2026-06-25 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71a92f95-dcca-3ae9-9f62-1ec789322911 | -8.85791 | -46.93265 | 2026-06-25 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7bbf830-4937-3169-8047-18068cbfbabd | -11.49422 | -52.92237 | 2026-06-25 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 925bb144-6601-3617-ac17-6cec1e46d197 | -12.74236 | -44.45252 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8210bb3-24bc-3ba0-bf99-b9a276c251f7 | -12.74391 | -44.45497 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 06efcd23-799d-3cda-9685-ea22b9c0f398 | -11.75168 | -48.83452 | 2026-06-25 04:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 406e4e01-ad2f-3098-9017-252f1a426bda | -12.73663 | -44.46097 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 73f33ad3-335b-372e-a701-256fab2e0cb3 | -11.94256 | -46.7488 | 2026-06-25 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d7ea31a-69a6-3630-a2ca-2bd342013e97 | -12.13884 | -48.26467 | 2026-06-25 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e6cac49-1c82-3dbb-9943-c89a89cc6970 | -10.3864 | -56.72215 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1339e8df-02b0-3043-80c7-82ca12b620c5 | -9.18427 | -45.32024 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f072b4b9-13f4-326a-9c05-18a2b45a2860 | -7.73112 | -44.17697 | 2026-06-25 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 425f1124-d794-3cda-a3b4-8ee5c7ad8f0d | -9.9845 | -47.73642 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7453a01e-e1e0-3d85-b419-cc8c62d93f5a | -7.63625 | -50.21607 | 2026-06-25 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c43e6272-8be5-3b55-9e9d-142184acf4df | -11.90547 | -56.85974 | 2026-06-25 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e510e44-9857-35f1-8cfb-ac0581dff104 | -9.10725 | -47.46315 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f5d6a79-2527-3084-903b-8c69354eb367 | -10.12861 | -52.11375 | 2026-06-25 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d77f5707-ac50-3d3b-b16f-b0e788538ad3 | -10.27672 | -47.6022 | 2026-06-25 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65190b23-1726-3a80-b0b6-c53be7454f78 | -12.45267 | -46.52342 | 2026-06-25 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed6a2c2c-767a-311c-b795-9cd2e1ab9569 | -11.25191 | -43.33075 | 2026-06-25 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 760bae2f-5c88-382d-94d7-e610324aab82 | -6.75769 | -46.3075 | 2026-06-25 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 698c29cc-ac99-3f03-bb27-029eb10e6166 | -13.19802 | -48.32186 | 2026-06-25 04:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f05244-c871-3e4a-8e1b-946972d9c3d1 | -7.75273 | -44.61487 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 509f6c41-9df5-30f1-ab6a-660b87916339 | -9.14104 | -47.98202 | 2026-06-25 04:49:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49cef484-e6d1-3584-aa0d-a8280b65242a | -8.12445 | -47.89196 | 2026-06-25 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 189d2481-9a37-3e8d-86ab-e821c4dc1beb | -10.38355 | -47.30523 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6062bd45-f03f-3f6c-8ac7-2a32e2911723 | -10.39306 | -56.76567 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c578aad9-400d-3b27-a00f-e0b0c4715d53 | -12.74274 | -44.46407 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6702dd05-0dfe-3da3-94bc-34cccfd072f5 | -9.20041 | -45.32257 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 693c4d91-2332-32e3-8bd3-625de1251cd9 | -10.38788 | -56.71367 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9648985-757e-330e-a63b-af8e06512ebd | -11.49358 | -52.92619 | 2026-06-25 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 735aef83-2429-3d85-bd2c-48d0f9832ed5 | -6.76071 | -46.3124 | 2026-06-25 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 119d1f38-c6e5-311c-b92f-442c3fad17b6 | -10.77227 | -54.11438 | 2026-06-25 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbfd23be-5fbc-3d4c-b13d-916f4e635e33 | -11.1994 | -49.41841 | 2026-06-25 04:49:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 585ddd3d-3bed-375a-a550-19549ee98aca | -11.56085 | -47.61863 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83ac358d-01af-3d91-84f3-f0d376da92fb | -10.9351 | -56.85921 | 2026-06-25 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54100dad-3caf-3ddc-870a-8e5fc0047124 | -9.36967 | -50.53026 | 2026-06-25 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0396d4ee-a93b-387c-ba5f-1efa63f8aa1c | -12.08093 | -54.61134 | 2026-06-25 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29d32a43-3cb1-3f84-a586-7eaf0658bb69 | -11.90324 | -56.87196 | 2026-06-25 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| becede59-d475-31fc-8f14-d59b64b38366 | -11.55721 | -47.61807 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6909484-6a0a-3dac-ad4b-5650ebba7cb1 | -9.36801 | -50.54076 | 2026-06-25 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7e107c3-ccf5-3fcd-95d8-5c62ff3232a3 | -7.74694 | -44.62555 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a23eec8-c642-3466-b9d9-d24f15471bde | -7.74282 | -44.62488 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3cc20a37-d4b8-35c4-ab4b-94b6ba07abb0 | -7.73979 | -44.61669 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 406cdae1-2efd-3b10-bcf3-a04b0488df97 | -6.97172 | -42.89148 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 345ce5a0-f599-3244-a77c-f9f8bd062491 | -9.62565 | -49.01537 | 2026-06-25 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c57093e-1be2-36cb-8294-b86c43c51be4 | -11.91195 | -46.62549 | 2026-06-25 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae20e7fd-5302-38de-95f5-1c57fb152a44 | -11.88464 | -51.75158 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 24b4c4de-fb0c-3eb5-bf37-2e56f16d4d70 | -10.38765 | -56.7663 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82a71857-9fb9-3a8b-b3ec-fc1b03000263 | -12.74949 | -44.4674 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9553aeb1-06e4-3ee9-8ed9-357ce30f1200 | -7.76043 | -44.61997 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5a8f7f95-ddf2-3f1b-9036-b2c4d26b50bd | -10.38209 | -56.72123 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46228337-005c-3c4b-81ef-1efab35de590 | -9.20127 | -45.32248 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1b2de7d-9e3c-391d-82e6-a611fcc03805 | -13.20516 | -48.32304 | 2026-06-25 04:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92f8a17a-c667-33cd-b357-1b4dcddb4a0c | -10.41448 | -46.7333 | 2026-06-25 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ec5280d-c030-35f1-aba6-5d634f66a805 | -11.63697 | -52.86412 | 2026-06-25 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52712aa3-3c13-3a02-be34-d5f3cb167608 | -10.37057 | -47.34238 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24fb028c-6206-39ea-a478-1c4a1ad30a6c | -8.57929 | -46.90799 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7898b1f1-f9ac-3db7-b8d5-96b2ce0b74c9 | -12.75011 | -44.46286 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e2080865-f54e-39f5-a171-f076cc1a9860 | -9.97386 | -47.73464 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 874915df-883c-3c7d-8379-0170e3d039cd | -11.87068 | -51.75293 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab85c3e9-9296-32a4-81ec-2dcad888a1b4 | -11.58299 | -47.44585 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d772ed55-a5df-379f-9959-ce00ec9e258b | -12.13529 | -48.26413 | 2026-06-25 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cfac8cdb-0f27-3bc9-b941-8e4b5ecaa4c6 | -8.12503 | -47.88817 | 2026-06-25 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbac09f2-e531-3d88-a295-25c19479b8d7 | -13.03315 | -49.93855 | 2026-06-25 04:49:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5bebb1f-660f-3d6b-a7f5-a8f984a10ba9 | -6.97139 | -42.89003 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f567541e-3807-3180-8970-6113ab609732 | -12.74174 | -44.45706 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c357109-9dc6-38b8-9bd1-8fd3145b0b8e | -8.06689 | -46.38938 | 2026-06-25 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1793d98-bffa-31fe-bd62-bc71006e71a0 | -10.77668 | -54.11066 | 2026-06-25 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f501224b-217a-31ee-9035-8ff6dde4b94a | -9.76921 | -48.25579 | 2026-06-25 04:49:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51b1d3dc-55cb-3bb9-b880-8b1e769f74d2 | -6.31228 | -44.64696 | 2026-06-25 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7be16ba5-8ca3-3794-a305-2846c0396820 | -11.88521 | -51.748 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| a736e5f7-d0de-35c2-8a76-af33ee59f350 | -12.73725 | -44.45643 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7cb06a1-dd91-3209-b8f6-1a8b8effef08 | -9.80429 | -48.91957 | 2026-06-25 04:49:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f216fa64-1e1c-3151-9896-3638cc336030 | -12.74112 | -44.46161 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 13fc48fc-79c9-3481-93f5-d570e7676cbd | -9.03953 | -47.26506 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1493e8e5-2a6e-33cc-a6d8-b8cc6d1e74fe | -11.92286 | -46.63171 | 2026-06-25 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e52858e-f034-3f25-9bec-d19c242955be | -6.90471 | -43.67933 | 2026-06-25 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd255eee-7e94-3455-b023-2c1a18ae189b | -10.24746 | -48.32621 | 2026-06-25 04:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bd11765-e133-332a-a436-484cdc5fcd39 | -8.33126 | -51.34839 | 2026-06-25 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9eb55d5c-9d12-349b-810c-b3d7ae1882bc | -11.92029 | -46.62842 | 2026-06-25 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b74df3f-3535-3701-bb7c-80111d20acef | -10.294 | -44.68959 | 2026-06-25 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27c38a3a-444f-3b30-8a20-99bd2a6532a5 | -11.91898 | -46.63133 | 2026-06-25 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f3b3b3e-c0e5-314b-9d67-bc399f96a3af | -7.72686 | -44.17635 | 2026-06-25 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab8a768f-4898-3f2d-be91-b06f80a491c6 | -11.5424 | -52.78197 | 2026-06-25 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d87cf85b-ee45-3304-a7cd-0a90a50db006 | -10.3663 | -47.34608 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 727c9c3f-2807-39d8-91b1-4970a7e2c455 | -12.13589 | -48.26009 | 2026-06-25 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c692addd-fb77-3c98-8867-db9e83de9619 | -12.74562 | -44.46224 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2041dfab-e7b2-39b9-9713-5aae3d0ad924 | -10.28973 | -44.68898 | 2026-06-25 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b674673-3e60-3e87-ad73-f24581145c12 | -9.57779 | -49.11961 | 2026-06-25 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e79431b-2f74-3121-9772-9bc6b8eef3b0 | -8.1285 | -47.88871 | 2026-06-25 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)
