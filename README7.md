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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa9562f7-240d-37a6-92c9-273d416be78e | -13.00353 | -44.8871 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2695c380-1419-37fd-9129-36ed64357349 | -16.21827 | -40.13889 | 2025-08-07 03:40:00 | NPP-375D | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1dcd8066-00d1-356a-8eee-9a2fbcc7b2cf | -12.55929 | -44.74859 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e51a643-888e-393b-a2b2-a299898f6edc | -11.80829 | -44.26485 | 2025-08-07 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c3ebfc8-3bae-34a3-9352-16a8e83a8311 | -12.70408 | -46.39446 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b364d2c8-b298-39ad-be6b-bcab2fd27c30 | -12.71267 | -46.38234 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b2aa405-fff8-3d8a-a1ec-8dbb3e7e78e8 | -14.52427 | -45.59591 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc5aefe4-bc1b-3e27-834d-5f76df7dd673 | -12.70957 | -46.39719 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fec2167d-54d8-33be-9254-ad3ca349493c | -16.21447 | -40.13798 | 2025-08-07 03:40:00 | NPP-375D | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 572ffd93-a3e0-38d2-a503-0fcc9469cbd4 | -12.53047 | -47.15113 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f4ac630-5bef-3795-9fdb-e92ef5a96283 | -15.93318 | -43.51557 | 2025-08-07 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ee2b79a-fb5f-3913-ab1c-ce41337afb50 | -12.70908 | -46.40101 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce468b8f-0263-3f9d-805e-95da1789a7b9 | -10.69999 | -48.87405 | 2025-08-07 03:40:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b16ce42f-b5ec-33f1-a51c-a2a9450bf889 | -11.74066 | -45.01555 | 2025-08-07 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9c5e0a1-df40-3c03-ac29-bec96a75abf6 | -17.19712 | -44.32587 | 2025-08-07 03:40:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c0e115c-4003-3dd0-96c0-245fa2bfcc84 | -18.73161 | -39.86862 | 2025-08-07 03:40:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 13d1b6ac-32de-301f-8d7a-8ca93555317a | -10.70879 | -48.86793 | 2025-08-07 03:40:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab8514d5-e34c-3fad-a0a7-f7e9bd9ac071 | -14.52906 | -45.60096 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 87368246-9985-387b-aba9-87091018f8fd | -16.21812 | -41.34342 | 2025-08-07 03:40:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b5c5ec7-5776-3db8-a40d-81de6527dd03 | -12.71871 | -46.38371 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a541226-59a2-3259-9f61-ff321e639389 | -16.04058 | -43.72559 | 2025-08-07 03:40:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b655073-489b-35c2-a663-d44bcd4c6e78 | -15.92841 | -43.51455 | 2025-08-07 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc435523-c062-36ca-a0bd-171f054ed614 | -12.54239 | -47.15775 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4adbba4d-af77-3bac-8816-d6af76154daf | -10.70108 | -48.8717 | 2025-08-07 03:40:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7d1b248-bea5-3a78-a035-9c70e12da268 | -11.78661 | -47.54014 | 2025-08-07 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 50eab921-a214-359c-9093-06e0f53e296b | -13.00898 | -44.88851 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12881c90-c765-3002-b2d3-a94c3b4c3eb8 | -12.72473 | -46.38514 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c366942-246e-33c1-b0d3-f6a21e2434dd | -11.89834 | -44.97168 | 2025-08-07 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e4de72b-ce97-3c82-96aa-6d7d6bfc15f0 | -11.8975 | -44.97601 | 2025-08-07 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b5bb354-8961-355d-9066-46cb39da93d0 | -12.33503 | -46.05901 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29896aa7-face-3bc1-94fa-e60f78db3cd1 | -11.75732 | -48.19249 | 2025-08-07 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e1caeffa-489b-3e02-a83a-89d87e93eaa0 | -12.52411 | -47.14976 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d017e0c-09d4-34d5-89e5-3ba2383b5869 | -12.54839 | -47.16439 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5a52ce1-2a3f-316b-9735-224233beee59 | -12.54943 | -47.15949 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 18b30aef-04ca-3921-88e0-7920d3c847a5 | -11.81436 | -44.26242 | 2025-08-07 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1950ce75-07bb-3eb7-b776-a581eef5b72e | -11.75862 | -48.18629 | 2025-08-07 03:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8f465aeb-634f-39f5-b48e-135c9db1ad73 | -17.20202 | -44.32698 | 2025-08-07 03:40:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 74fdfa0d-a51c-3488-ba1e-ba22c1426edc | -16.04164 | -43.72013 | 2025-08-07 03:40:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b31f89a-4ed1-395e-ae1f-f57bd0f4fc49 | -12.34101 | -46.06026 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfbedd98-75c0-3899-a83e-9aa4854402c7 | -11.80761 | -44.26836 | 2025-08-07 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b66acce-a240-3c88-857c-b22c8bf7ec2a | -15.7764 | -39.37408 | 2025-08-07 03:40:00 | NPP-375D | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 36b17a14-05ec-3934-9288-e990b4e9e44a | -14.52348 | -45.59975 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3ab95d9-96e2-3fad-ab86-614fbc09ab9a | -11.75252 | -44.95545 | 2025-08-07 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 346891a1-df2b-3d6a-84b1-fea4ff6a09be | -11.73501 | -45.01428 | 2025-08-07 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2db8792a-7d5f-36f8-b13e-2fbf7ca5f714 | -15.34657 | -46.34346 | 2025-08-07 03:40:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa61792e-0af5-3e85-b7da-ec8590348b31 | -12.53685 | -47.15239 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9b7dddd-2709-3974-895f-54480f2c1d2f | -12.54882 | -47.15879 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88d0026f-9f2b-3347-a68c-e40ffccee6b6 | -11.7399 | -45.01938 | 2025-08-07 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cb6f9aa-fcd4-3045-89fa-6dc35ae469a8 | -12.32905 | -46.05777 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea378c88-4c68-3353-a712-e2e946d54163 | -12.99809 | -44.8857 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c74521c0-59f7-3bfe-9d15-026b22668b92 | -11.77436 | -47.40127 | 2025-08-07 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a461d24f-1c01-3954-8141-54dd46a1aa30 | -12.71009 | -46.39603 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0376e94f-6ec2-370d-8d04-c3e876809996 | -14.56069 | -41.15214 | 2025-08-07 03:40:00 | NPP-375D | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5283948f-e0d8-3ada-b1b1-033d0e21114d | -15.93213 | -43.52091 | 2025-08-07 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b3990d0-7fb7-3c06-9b96-c767c520de45 | -12.73117 | -46.38542 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa273f15-8fd9-3397-8ac4-2bd89403d7e3 | -12.34583 | -45.75933 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3041999-6cd9-3256-a93a-598665904a98 | -14.52748 | -45.60866 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 29dd9bf5-b55e-3b29-aac7-cfff1f4e9db9 | -12.34011 | -46.06477 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e95b069f-77ff-3261-8917-5a34bde54d21 | -12.34699 | -46.06153 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a9d1910-bf5d-30b5-83ba-ef7c4b01a742 | -12.37742 | -47.04996 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e221a1c-518c-3990-ad30-9c287a0d4e02 | -10.70991 | -48.86569 | 2025-08-07 03:40:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c45b45d8-0929-39b6-9b04-faeff026f47b | -14.53623 | -45.59445 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d3512b7-3958-3f09-a696-66c5c50a7f53 | -14.53465 | -45.60216 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4b138344-7d8f-38e7-85f8-8fea40f629bb | -12.71165 | -46.38721 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c1d84eb-4cd6-32c6-88f4-f064f0050adc | -14.52269 | -45.60359 | 2025-08-07 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d73513a-9831-3261-ab23-60d39dd37ce1 | -13.00424 | -44.8835 | 2025-08-07 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c311a5f-4450-39e7-a4a7-a8e74057a87c | -12.37633 | -47.05517 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 023ada59-053c-399a-a953-5968a11e4b98 | -12.37578 | -47.05211 | 2025-08-07 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57fefb01-1c76-355a-9db5-57a7cfb50d45 | -11.78154 | -47.53141 | 2025-08-07 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cec58aaf-f676-3d06-9d12-8fcad392da5a | -12.73209 | -46.38082 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac6b8861-11a9-33ea-b208-1e942edb5776 | -12.71768 | -46.38864 | 2025-08-07 03:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39828ef6-9b3a-3c01-ad84-61e36d934505 | -12.32815 | -46.06227 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 705487f0-2179-3bad-8da2-c87d2e80fa70 | -12.32995 | -46.05327 | 2025-08-07 03:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad01b01f-1fa6-36c0-b03d-9544db670c77 | -22.33994 | -47.20505 | 2025-08-07 03:42:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f030b907-4c2e-302b-8dd2-547c69909996 | -21.46276 | -49.65276 | 2025-08-07 03:42:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 05fb90a9-bf2a-3598-bf2e-aaf9add2c55f | -22.03708 | -43.21632 | 2025-08-07 03:42:00 | NPP-375D | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 703b32bc-4468-3290-bb0e-8cdc563ec070 | -22.33916 | -47.2086 | 2025-08-07 03:42:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c32f58d6-76a0-3ec4-8784-2a542360ccea | -21.87083 | -42.88235 | 2025-08-07 03:42:00 | NPP-375D | ALÉM PARAÍBA | MINAS GERAIS | Brasil | 3101508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a043cf2b-56f3-3983-a58c-4127df215877 | -22.73705 | -42.96114 | 2025-08-07 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1e18b216-0373-3701-afcf-66300bd2b7c9 | -22.03365 | -43.21308 | 2025-08-07 03:42:00 | NPP-375D | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b7529a24-7b11-3444-b950-56e8751f08d2 | -21.23751 | -49.09028 | 2025-08-07 03:42:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 9eaa7f7f-e71d-3de6-a0fb-64092ba4fb4b | -21.23345 | -49.08271 | 2025-08-07 03:42:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 281f7591-94c9-32ac-b427-d1129fc15263 | -22.33388 | -47.20716 | 2025-08-07 03:42:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b3099c2-c6ef-384b-b8c2-6801e2395bec | -21.4739 | -49.66138 | 2025-08-07 03:42:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a04aaca4-7a26-3d40-a17e-5bd01770f91d | -21.46147 | -49.65818 | 2025-08-07 03:42:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 7dbc862f-1785-318d-b42f-228907bf6457 | -21.11089 | -47.03926 | 2025-08-07 03:42:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd8b9785-76bc-3bbc-b584-5ad1a359ab32 | -21.23236 | -49.08749 | 2025-08-07 03:42:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 648a719c-ba69-3186-ab4a-f23f64b1450e | -21.23977 | -49.08069 | 2025-08-07 03:42:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 6be9cdf4-341d-364d-bbaf-cc43c148dad0 | -21.23256 | -49.08413 | 2025-08-07 03:42:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 891a10d5-a65a-3462-b475-3bcc35dec93b | -22.73854 | -42.96173 | 2025-08-07 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e25ae39-f702-3121-8a26-b6568b0b0c3f | -21.23867 | -49.08538 | 2025-08-07 03:42:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 4aab4061-e21b-3c0e-908a-3270b8fc8bcd | -21.46898 | -49.6543 | 2025-08-07 03:42:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 5f247106-f740-3c0e-921b-705fbb6f19d3 | -22.03703 | -43.21818 | 2025-08-07 03:42:00 | NPP-375D | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d8e7648-fd62-364e-a038-14c8b8606970 | -21.4677 | -49.65973 | 2025-08-07 03:42:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 74c1852f-01e5-3cb6-a47c-d839b0564c7d | -22.03289 | -43.21546 | 2025-08-07 03:42:00 | NPP-375D | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd935648-f159-342b-9be9-640035de8de1 | -20.33547 | -41.44823 | 2025-08-07 03:42:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3427e799-e345-3736-bfcf-cee2c69d5946 | -20.33152 | -41.44785 | 2025-08-07 03:42:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 00f3c96b-0301-3fa2-9ef1-8b73d601ac24 | -19.64776 | -45.45126 | 2025-08-07 03:42:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff7bd8dd-a061-36e9-9ef4-68e43cc8f8bb | -18.84453 | -47.04963 | 2025-08-07 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1563347e-1673-34d8-99e1-11f29c84522b | -18.84824 | -47.0526 | 2025-08-07 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README8.md)
