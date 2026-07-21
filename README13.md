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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39c43e6d-0390-307f-9663-da31e95f2bdb | -17.46117 | -47.15781 | 2026-07-21 05:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caf5a509-4c67-35cb-9896-dd4596ec9513 | -17.58528 | -47.50593 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 57ee2182-d4d1-379f-90a1-e71041e457f5 | -20.38143 | -46.59616 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 764b4d42-78e4-3516-b3b8-0dd6762fc5d3 | -20.43736 | -46.47558 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d484d9-96dc-36af-9fee-f70a4d003162 | -18.54349 | -56.81618 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 45be8e3b-999f-3dc9-b449-5850092ebbde | -20.3757 | -46.59935 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d43138f-ee9b-3612-bf1d-ce69d4fddf40 | -16.80565 | -54.58915 | 2026-07-21 05:06:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6552157b-afd9-3031-8643-b22b7478479b | -16.80898 | -54.58971 | 2026-07-21 05:06:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74aef31a-ad3e-3b26-837e-63b4b940a034 | -20.51602 | -48.8619 | 2026-07-21 05:06:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| beefe5b8-79dc-3fb9-b987-e4e4809e293a | -19.18293 | -47.3662 | 2026-07-21 05:06:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3c8a233d-8b46-3f4a-9c9f-3033047dbf3f | -20.89102 | -57.48495 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7002cfe0-6d5c-3520-9f7c-3de616945719 | -20.37541 | -46.60222 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4718c6f-3217-38a9-8330-0a366d6c998d | -20.37001 | -46.60225 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbc7f183-9b5a-3794-8a62-89202e55afa9 | -15.69786 | -56.12457 | 2026-07-21 05:06:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac5df9c5-a4aa-320a-a649-54fb37c12062 | -17.58859 | -47.50857 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d018a155-e8c1-3c4e-96bd-177559b72759 | -19.61194 | -47.65098 | 2026-07-21 05:06:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43012157-c840-3f0c-a7d9-fb622b7c09dd | -18.54685 | -56.81678 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 686d85a6-10d3-3f0c-bda0-a6870a6328f6 | -18.54287 | -56.81991 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5cc967f9-bcfe-397b-a627-91913be912be | -18.54747 | -56.81306 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0d39ac33-eae7-360b-a9b0-3c731055daec | -17.86108 | -50.51522 | 2026-07-21 05:06:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b19f050d-218d-3d86-9665-573886fd6ef0 | -20.87379 | -57.50521 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f966b752-d224-307f-91a5-8bcf2a61b887 | -17.58374 | -47.50805 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10b80d37-dca4-37c6-bf1d-cfc82b5a6663 | -17.46183 | -47.15213 | 2026-07-21 05:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5661986c-b621-3f7c-ba2f-2229cf79a83b | -19.61259 | -47.64513 | 2026-07-21 05:06:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f97fb1f7-6936-3d01-a543-5d6a5de63130 | -17.57952 | -47.50198 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2bdf19c-2e2e-3afb-bcf1-6011ba0c0a15 | -20.89039 | -57.48875 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ec9b3948-9dbc-319e-b076-328f8fa54f4f | -17.58043 | -47.5054 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 232328ac-5d1c-3cfb-9f3f-d970447a0c0e | -18.55295 | -56.82174 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 599adf6c-a0e6-3d8b-b1c5-61a4ffd9a5aa | -17.58462 | -47.51134 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5a401554-d883-3f56-87db-30693f2bfa01 | -20.87357 | -57.48559 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5eb82467-995a-3f06-84a4-7d76532a3dfc | -18.55419 | -56.81427 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 4948dd59-211e-3a1e-b48e-6e4b9f97a2a2 | -20.35857 | -46.60871 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ff55f93-ee3a-3a2c-97d8-9d26a8b3bca3 | -20.36398 | -46.60847 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7636d859-1067-3bfb-9bd1-534f4514c156 | -19.18843 | -47.36664 | 2026-07-21 05:06:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c3270d2-cf62-395a-85d4-9a176663c521 | -18.55083 | -56.81367 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 2fb29ed0-2612-39f7-8900-dc95b61b3328 | -19.60767 | -47.64442 | 2026-07-21 05:06:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4826bf1-f55c-39e0-8ce3-cf20136bbf8d | -18.54623 | -56.82051 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 40e1ffac-e1b6-3f50-82ca-27d9c9f771ef | -19.18793 | -47.36681 | 2026-07-21 05:06:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 127157e3-3ec3-3ad5-a46d-6cec56fcf288 | -17.58947 | -47.51187 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e1615a3-f37c-33a0-8509-b47d5d78ef12 | -20.87231 | -57.49319 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 66cc3f51-6516-395a-bd91-58aedc918e4e | -20.37508 | -46.60538 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 050c0fee-32f2-3ddf-8098-340c65a8ed89 | -20.38108 | -46.59947 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27d514f7-d1fe-39c3-9a3d-24fba5a8b70f | -20.48239 | -54.98195 | 2026-07-21 05:06:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bb840f3-5605-3f12-a930-0ec26432db5f | -20.6195 | -55.69784 | 2026-07-21 05:06:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78002661-87a0-3a01-9da5-356bb1db4632 | -20.35884 | -46.60609 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bab42f2-4d9e-3ff1-8e48-f94fd68bc808 | -20.47902 | -54.98138 | 2026-07-21 05:06:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7a280af-55d0-3021-9ade-b9ae989edb31 | -20.43229 | -46.472 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f2c82c9-cc5c-3010-8c06-d41f2db43b07 | -18.55234 | -56.82546 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 8c0f1fd7-fd61-32dd-b4b2-46194a324141 | -18.54897 | -56.82486 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.9 |
| 2dbfdc18-e3ff-3fe8-99a8-2f1275596ba4 | -18.55021 | -56.8174 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.9 |
| c1ac454b-aa3e-3c52-97ec-e9e458981276 | -22.37891 | -49.78669 | 2026-07-21 05:06:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 90a69411-7891-36b9-8017-548dbaea6d67 | -20.70325 | -50.53128 | 2026-07-21 05:06:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e2fb829-ad4b-38f8-97ad-b3c6390462fd | -17.58437 | -47.50256 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb84d62f-fd9c-332b-94f9-cb4fbedef077 | -19.18359 | -47.36013 | 2026-07-21 05:06:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9cce90f1-3e2d-3166-81ac-8958dd07248a | -20.51741 | -48.86064 | 2026-07-21 05:06:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0dab122-1870-3a34-9c0f-cc8129de1595 | -17.45687 | -47.15166 | 2026-07-21 05:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cbb6dad-f358-371c-9d29-e6365d085542 | -20.88703 | -57.48812 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 271e4947-3bdf-34ee-a24a-6631e2762a0a | -19.18343 | -47.36603 | 2026-07-21 05:06:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 99a85515-74a1-33ae-807f-c2fd822ee990 | -20.36425 | -46.60591 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 794843de-d4e4-3469-b74d-1653ae10afdd | -20.62283 | -55.69842 | 2026-07-21 05:06:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38361319-36cc-3e91-8016-74a0cec31e85 | -17.86507 | -50.51577 | 2026-07-21 05:06:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80566aaa-b73a-3749-be7f-49a62168d76c | -18.5548 | -56.81055 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c0f3bba5-8afe-365c-8e49-167cce9090c0 | -20.43268 | -46.46828 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12643ed8-224f-3ed7-947f-aeffabf62ece | -19.60831 | -47.63863 | 2026-07-21 05:06:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a42db5f-8240-3769-87af-7702c9225e75 | -17.6557 | -48.20481 | 2026-07-21 05:06:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 783592f9-665a-302a-8780-ff1362cf87dc | -17.58312 | -47.51342 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8110b4dc-5830-3969-95ab-85391de5a15b | -18.55357 | -56.818 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 3ce21e61-cbe0-3421-bee7-618494529947 | -20.376 | -46.59645 | 2026-07-21 05:06:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53793061-4e70-3f91-b9e6-00453a367d97 | -19.71669 | -53.2418 | 2026-07-21 05:06:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c2b818d-7238-362d-974f-f81667451bab | -19.60895 | -47.63279 | 2026-07-21 05:06:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cba6467a-5aed-335a-a9bf-d41947f52cab | -17.5811 | -47.49983 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe73dedb-1f75-3c11-a97d-4062949fbc95 | -22.15071 | -49.15297 | 2026-07-21 05:06:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ab02478-1f19-318f-bfc4-5ed29d7339b1 | -17.58798 | -47.51389 | 2026-07-21 05:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a23cdb7-110e-34ae-9b5d-755bfd8fd5ae | -18.55631 | -56.82234 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| c79d5db6-8162-3500-9e26-3ab9dc6c5d9a | -18.54959 | -56.82113 | 2026-07-21 05:06:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 4c909f8e-c5ca-3641-931e-ecd6f25de463 | -20.87294 | -57.48938 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7130de96-f7c1-3919-a8df-d3ba4f8ec1d2 | -20.6991 | -50.53073 | 2026-07-21 05:06:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9000e40b-1ed0-32f4-ae6c-0c3e7aa20eb3 | -23.14132 | -48.6746 | 2026-07-21 05:08:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e91e36b1-20aa-3e3c-9010-9a6ab38d7d01 | -25.03489 | -50.7269 | 2026-07-21 05:08:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb600a96-5966-34ad-bccd-2fe4735d3560 | -22.79495 | -49.34334 | 2026-07-21 05:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9297bee-29c0-3d12-a17f-7d0fffd455f8 | -22.80029 | -49.34774 | 2026-07-21 05:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5092690b-8efb-35c6-99ee-550fe0baa8f3 | -22.79902 | -49.34886 | 2026-07-21 05:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 420495ff-1baf-3598-96d2-3a20bcf8b9bb | -22.79626 | -49.34219 | 2026-07-21 05:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1e5a7d4-d4ea-3ca0-ac34-b627b4308051 | -23.77858 | -49.0421 | 2026-07-21 05:08:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73c0cdf2-09c7-34ca-a42b-206e51ca08b6 | -23.5614 | -47.52477 | 2026-07-21 05:08:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c56aece2-baec-3fe2-8341-e6e254272b94 | -23.56205 | -47.51806 | 2026-07-21 05:08:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 30a0ded4-dd98-3f24-92cf-9026042e1609 | -23.13646 | -48.67432 | 2026-07-21 05:08:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbd609c5-3f8e-3499-ad46-f6d114b449cf | -23.56726 | -47.51879 | 2026-07-21 05:08:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ef91d0f1-b52f-30f8-b702-72512ef8b88e | -23.28975 | -46.16148 | 2026-07-21 05:08:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 07c3c280-401a-3cc4-b5c0-230dfd1dea63 | -23.56173 | -47.52137 | 2026-07-21 05:08:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 05667f6e-a179-3382-8094-b6d3bb91ebf3 | -26.31236 | -50.26579 | 2026-07-21 05:08:00 | NPP-375D | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 804b2c99-9ea2-3283-8fa0-c61937d01d47 | -23.29542 | -46.16204 | 2026-07-21 05:08:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0036a00a-6502-31c8-a62b-98600b539020 | -22.79568 | -49.34724 | 2026-07-21 05:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da29340d-05cc-34ce-8543-862f36755d80 | -23.56694 | -47.52211 | 2026-07-21 05:08:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8872e3a6-6870-3525-b1ee-3da2294bcff6 | -22.79955 | -49.34387 | 2026-07-21 05:08:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08517fee-b9ae-371f-8a8b-bb0d0d9e676a | -13.3032 | -45.1045 | 2026-07-21 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 69827add-f31c-3596-bd95-ebe672fa0761 | -13.3221 | -45.1246 | 2026-07-21 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 08a1cacc-501b-3786-a2a9-4b32cfa7018a | -13.3023 | -45.1511 | 2026-07-21 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| be51c85f-87f1-3586-abcb-d401aca57871 | -13.3028 | -45.1278 | 2026-07-21 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 33b46d6f-1c85-31b7-b80d-bfb9b9223c43 | -18.5472 | -56.8343 | 2026-07-21 05:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |


[Clique aqui para ver as próximas entradas](README14.md)
