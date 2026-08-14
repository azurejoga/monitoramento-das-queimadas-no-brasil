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
| 91e18ffe-dfa2-3d7f-b1b5-2b248718ea02 | -6.91112 | -43.63821 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04ec353b-8fc5-3037-9653-e4f9d4993c85 | -6.09185 | -43.97909 | 2026-08-14 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11440513-4880-36b6-9f1a-3ae9ed3779c0 | -6.41157 | -39.25745 | 2026-08-14 04:12:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f09b0a5c-bca1-3ebd-b121-e3510a9e07dc | -7.02544 | -41.44239 | 2026-08-14 04:12:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f84344ce-8e28-395a-97c0-0112b18c2d30 | -6.40713 | -39.26394 | 2026-08-14 04:12:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b8ba4254-ee08-3088-bd94-a41ebbe03218 | -5.79861 | -43.64351 | 2026-08-14 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2e3e78f-a53a-3bcd-93bb-2b36b300c0d2 | -4.50792 | -42.54307 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5022a7ba-4edd-3f73-87e3-c29bd9735276 | -6.91553 | -43.63445 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4961343-80d0-34ae-bc1c-a141027b3560 | -2.69321 | -48.2139 | 2026-08-14 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c64d64ab-46d8-318a-94fb-3aa0986441fd | -4.27228 | -49.36573 | 2026-08-14 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e9a686b-c333-3ab2-97e5-65fd8385b58b | -6.9148 | -43.6388 | 2026-08-14 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f27304d-6916-3ee9-a368-83d9606c9277 | -4.49652 | -42.5454 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| b8fadb14-3125-3b50-aec5-96345a29fec4 | -6.86581 | -42.92034 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 42b9fe4c-8adb-30fe-aa7f-27ac40a7260f | -7.02487 | -41.44593 | 2026-08-14 04:12:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8b5e6de3-5da8-341b-aa58-8449183b6a4e | -2.64474 | -47.9842 | 2026-08-14 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d430b6e6-0121-34ea-b833-3c914919f43e | -5.55497 | -44.11081 | 2026-08-14 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39f76d8e-140b-3f85-a922-c24850a82b9a | -6.09075 | -43.98096 | 2026-08-14 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c543326c-cbdd-3916-878e-c84bbd5f6be5 | -4.49943 | -42.55002 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 95fe3ac1-27a9-3c86-ac9b-f6b3bdb305f0 | -6.87991 | -41.9549 | 2026-08-14 04:12:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e6f5963-113f-3c77-8462-b245a08a845d | -4.49094 | -42.557 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 23851afe-591e-3295-b246-47eb62f2f74c | -6.27247 | -39.68593 | 2026-08-14 04:12:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e5f4d5ac-8846-3f17-8470-c79cfd925a37 | -4.42737 | -46.30278 | 2026-08-14 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47f0643b-6233-386d-afb4-9028726b9013 | -4.48736 | -42.55643 | 2026-08-14 04:12:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 37feebf6-bf61-3226-8b77-5b0b58831c57 | -6.90841 | -43.92646 | 2026-08-14 04:12:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22eac404-fe2e-3e34-bfb9-14c9c0c7767a | -7.6033 | -42.74048 | 2026-08-14 04:12:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1c5f44d-8eba-3a3a-a244-3b394911a6bb | -5.78335 | -45.05149 | 2026-08-14 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b0df82-0b74-333d-814d-6f449d7db812 | -2.79594 | -49.58302 | 2026-08-14 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c52f4e63-70b3-3ecd-8543-1cc20d19d106 | -6.84297 | -42.90426 | 2026-08-14 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a29e85ac-0315-30bc-bb12-b20e6ebdd457 | -6.41019 | -45.67585 | 2026-08-14 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 03939dfa-bf54-30b2-8930-3e11705596e0 | -6.27251 | -43.27936 | 2026-08-14 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebd14fc5-2306-365c-a54f-495d7facf5e7 | -4.73829 | -48.01941 | 2026-08-14 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 037bb4ff-505b-380b-b714-215d951c5503 | -11.32102 | -45.21528 | 2026-08-14 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5874792f-1781-3d2e-9b33-526a7faf5bec | -11.06226 | -50.94987 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a42ffd92-36be-3696-a8fb-261560b14888 | -14.47607 | -45.69598 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5c533b8-1adf-3736-a273-95ff13e9d6c6 | -14.72197 | -47.15046 | 2026-08-14 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5f25bee-44fd-3e50-8fa3-8563ce68c629 | -13.6822 | -46.26776 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 96efcdc6-e293-325a-9d5f-86a366f41c6e | -11.45679 | -44.56077 | 2026-08-14 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c2259b4-49b3-318d-ae34-5e55076ec2bf | -14.24264 | -45.4107 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1524e3c4-5b7d-3a7b-a0ec-41d45fd93f57 | -13.27619 | -54.23597 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9555e0ff-23f4-31e9-bb07-654afd852a0d | -10.98697 | -50.54778 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bf62e3a-c8f9-3413-896a-8384ee2273f2 | -14.48058 | -45.69212 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a141c051-74f1-3b73-8843-bc210a356f25 | -9.12436 | -46.39438 | 2026-08-14 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1d62a5a-9205-3d68-8dd0-aac0c6e41bf1 | -7.60799 | -46.4656 | 2026-08-14 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 584e41a0-58db-34be-bc1e-4f5e9645e8dc | -14.72599 | -47.15123 | 2026-08-14 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c13a1ed0-9b5b-3f7a-b78d-fc60bb729e6a | -7.7064 | -46.23683 | 2026-08-14 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d7ebbed-2cca-339c-8534-3bec8361ae85 | -14.977 | -46.60062 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb01eb72-80db-32f7-b2f3-22a79a009b90 | -14.60035 | -46.75424 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95209874-7dcf-3e8c-ae18-be10969ba291 | -13.27733 | -54.23045 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 508ab27f-562a-37dd-b06a-f91ac9456cae | -11.47062 | -44.56761 | 2026-08-14 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0272fb1d-9884-3936-b5a8-c41e52223a6b | -14.24187 | -45.41513 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55f37b1d-329c-3d44-922c-177a78859071 | -13.38639 | -42.39374 | 2026-08-14 04:14:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40cd7ebc-7270-3d67-a169-4315588097dc | -12.72661 | -48.43616 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2cab758-8287-3ab3-92de-5239dfed2a61 | -9.98262 | -53.95831 | 2026-08-14 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7ccaab31-24e9-3979-a898-d0600c6ba02d | -9.98196 | -53.95116 | 2026-08-14 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 595c6e2d-52d5-34ea-8a9f-6b01e58e6662 | -13.76629 | -42.61905 | 2026-08-14 04:14:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1cb6b5d5-969e-389e-adb4-cc6b58959104 | -10.29506 | -46.65342 | 2026-08-14 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49c6bf8d-1faa-34e5-92c5-da48b6427006 | -13.23687 | -54.2624 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d396060a-5155-354f-9efd-9376e63e30df | -13.56218 | -46.26424 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3fb3e3ed-6cb4-39ae-bffa-4b8d5c9cc9fa | -13.2838 | -54.23185 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e8231a7c-cb2b-3d6a-956b-ad2a50b6fd86 | -13.64939 | -46.2721 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff7d0315-1467-3753-9604-889b52c53c41 | -13.27423 | -54.2128 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0519fc5-c7cc-3533-b68d-f6f292e7e1b0 | -15.13696 | -41.55687 | 2026-08-14 04:14:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d30db8e7-714a-3052-a7e5-8b474535c41a | -14.73001 | -47.15201 | 2026-08-14 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 070c34b7-d82a-30a6-9144-16971f77425a | -14.47545 | -45.69364 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8bd5f01-04f5-3aeb-92b8-3e215b9928de | -12.76293 | -44.55377 | 2026-08-14 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61a46f70-b6a6-349e-b80d-dd010b654db3 | -11.27125 | -47.69343 | 2026-08-14 04:14:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 117b521c-705b-3b4b-8751-fd9cd306d350 | -9.07407 | -39.967 | 2026-08-14 04:14:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 24aa1e11-9327-39a5-aba0-919a4edc49cb | -9.97711 | -53.95101 | 2026-08-14 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1a8e030-e2c0-32b5-8b27-890c5cbe9414 | -11.94303 | -46.31985 | 2026-08-14 04:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e0eb8e3-1736-32f6-bf1c-33116718ab2f | -7.60728 | -46.46975 | 2026-08-14 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92b40725-d6a0-32a9-ab87-b259de5e1da9 | -14.95041 | -46.61449 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3eaa0f6-f2dc-31b6-af05-e471f2bf4459 | -14.62772 | -42.52437 | 2026-08-14 04:14:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fc082937-e779-3cb2-bc32-96f08e802318 | -11.07467 | -50.94477 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 342a46da-203f-345f-804a-f6620504d5c7 | -14.9322 | -46.62673 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ee395af0-a677-347d-9f8f-5ddfd01e4781 | -7.71564 | -46.23412 | 2026-08-14 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69e44eb2-3f19-3d5c-8f9a-5100006e235b | -12.71661 | -48.4395 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96a9dd92-c89f-3b8a-b227-01b008c5a696 | -13.28491 | -54.22643 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8a835b8b-74ab-34e6-a768-6a2aa6470bd2 | -14.95676 | -46.60125 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6b8004b-aba7-33d5-b7ae-1684ddbc5966 | -14.47026 | -45.68556 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b1e9a70-cceb-3483-b1e2-0e1adce745be | -11.31265 | -45.2186 | 2026-08-14 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48ea194e-e936-350b-8978-35ade6e588e2 | -11.47102 | -54.61802 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5c1bef2-ff09-3771-a932-74efcbf9e2aa | -11.49275 | -54.61603 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1c623578-bd96-39fb-9e21-1f6558f2ca13 | -11.48895 | -45.09626 | 2026-08-14 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77e8830b-c88b-3ddd-a859-7caa1ea94ce6 | -14.47397 | -45.68624 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61bbab62-6795-37a9-bcaf-5ac02f8d5cf8 | -14.97308 | -46.60014 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01df7e07-aaa9-3ae2-9442-7299c6488092 | -13.3903 | -42.39072 | 2026-08-14 04:14:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 9c4c1062-5a8e-3754-90a0-a8a90bda65d8 | -7.61232 | -46.46637 | 2026-08-14 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1a96836a-099e-37fb-b43a-f2b89034a19e | -11.07538 | -50.94109 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5894fd37-c579-3df0-945d-5e852ecf2661 | -13.28162 | -54.23728 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5a5d7fa7-b46f-3869-a7e5-f44994aca30b | -14.74545 | -48.23704 | 2026-08-14 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b6f906f-8801-30b8-a2fc-575d96bfbd28 | -14.46945 | -45.69009 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb8776e9-9df2-3c72-8377-29471f34caa6 | -13.38363 | -42.38961 | 2026-08-14 04:14:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b65a1854-4aa4-3c8f-826c-8e021cc36687 | -12.03355 | -47.81682 | 2026-08-14 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 058e6c3f-34ac-3c62-b3f3-eb54cf87d980 | -14.45533 | -45.69926 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0933277e-05e3-3782-87a4-1ffbe4ed5b79 | -14.4651 | -45.68705 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75d901b6-cb8b-34d4-adfd-bdd3c64cf248 | -11.47499 | -44.56396 | 2026-08-14 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9378ff65-7ea6-32dd-8a88-cd5779a8a5b8 | -11.31724 | -45.21461 | 2026-08-14 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9f75e37-beee-391d-b975-a07fd43a4d1d | -13.25325 | -54.24879 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebffc2a0-ffdf-3cd7-a65e-dc3c7cfb9feb | -12.71124 | -48.44314 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2a840e3-0a89-3f76-ba50-606e356d120e | -12.02327 | -47.82345 | 2026-08-14 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README13.md)
