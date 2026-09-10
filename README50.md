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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5adc84e2-1a9a-333b-9931-04c18954785f | -7.587 | -45.6804 | 2026-09-10 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| da92d983-b377-3fd7-a78d-d9631442a682 | -5.7569 | -45.084 | 2026-09-10 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f77838e0-8da1-33bc-8093-756d8e65ec72 | -9.0059 | -65.4186 | 2026-09-10 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 515e876a-6d96-3e5d-9fce-cf3ed5b4da6d | -7.1009 | -42.1327 | 2026-09-10 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 76d86827-7d9b-3e28-b46b-0a9fca1e6e3f | -10.6798 | -46.0858 | 2026-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 41df0d51-a34e-3b04-958d-5d05d25c244d | -6.7077 | -45.4635 | 2026-09-10 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| d8e96696-5552-391a-ac09-38da5997d6ea | -6.5637 | -62.8908 | 2026-09-10 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 52d264a1-62a2-3f1f-aefe-676eb163a45b | -10.2362 | -45.2775 | 2026-09-10 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 320.8 |
| a2946ea2-74d6-3a0d-bfef-e5ef6af4ce5c | -10.2753 | -45.2038 | 2026-09-10 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| b03359cd-2162-3339-929f-9a76a1039606 | -8.7253 | -62.4177 | 2026-09-10 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7d9a30f6-7f3e-336f-98a0-152e50bef053 | -10.6611 | -46.0655 | 2026-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 73c35d95-64f1-3344-8390-fecc3b61f687 | -9.6944 | -43.4453 | 2026-09-10 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 46004b20-5b32-3961-a914-d937d1adb6f5 | -10.6801 | -46.0631 | 2026-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 249.3 |
| 725f6eb5-4402-37a0-a1d3-01f4fda4e680 | -11.4026 | -43.935 | 2026-09-10 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 224.3 |
| a690badc-db84-30aa-a88f-5641f210bedc | -10.2552 | -45.2751 | 2026-09-10 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 321.0 |
| 71ab7401-5fb7-3041-aab1-bc28bec98db5 | -6.9701 | -59.0272 | 2026-09-10 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e8635e28-9421-39f5-baeb-ae1fee4f8040 | -6.5453 | -62.8914 | 2026-09-10 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 48a16f3c-fe9e-3d3c-87dc-91636511850d | -7.4976 | -45.2814 | 2026-09-10 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 447ad9cb-e6bc-3582-bc06-b99305fe1c56 | -6.7678 | -58.9003 | 2026-09-10 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b065affe-ac76-3151-a855-9b5c3890f801 | -3.4028 | -60.3232 | 2026-09-10 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| c288a21c-d142-33ec-bf49-2d7f53108ba1 | -10.2358 | -45.3004 | 2026-09-10 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 347.0 |
| d5ab5229-9224-37b2-b786-093f9aa1fd57 | -9.7885 | -43.5036 | 2026-09-10 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 245.2 |
| fe792006-e8d7-3760-90b0-99204436e831 | -6.7864 | -58.8801 | 2026-09-10 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| d4dbad36-9dd2-3281-a69a-cc2db632226b | -10.7488 | -60.7483 | 2026-09-10 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a903be92-730f-3d9c-a350-6e2a6579700c | -6.7695 | -58.6097 | 2026-09-10 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| cfa2f91d-7e08-3ffb-a726-311898619223 | -8.9412 | -44.3995 | 2026-09-10 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 50a4c478-aaff-3b5e-8911-ac610d01d53d | -8.7254 | -62.3987 | 2026-09-10 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5270fb5f-2e90-3c9f-bf6a-bd8241472f30 | -7.5167 | -45.2569 | 2026-09-10 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a6ddd766-59ce-3e14-b9c2-0fb32286db5e | -10.2549 | -45.298 | 2026-09-10 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 388.6 |
| 6ccebd36-f990-307c-bbd7-57f357447eb5 | -10.6981 | -46.1287 | 2026-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 20d3883f-91f2-366e-a4db-0fa2c7f468fe | -6.7863 | -58.8995 | 2026-09-10 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f589d4f9-71f5-3dd7-b33c-0e17d698237b | -9.6947 | -43.4217 | 2026-09-10 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 208.5 |
| 908e1b0b-6945-3916-8f53-ad31044be525 | -10.786 | -60.7848 | 2026-09-10 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b8983180-4623-3332-bd9d-82e584ea8e97 | -7.4976 | -45.2814 | 2026-09-10 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| cb4998b4-be6a-3013-b38b-2ef1f122799b | -7.1009 | -42.1327 | 2026-09-10 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| c9387ae0-977e-33c9-8203-4a52a9267c52 | -3.4028 | -60.3232 | 2026-09-10 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 131.6 |
| f44ad272-fab6-32b2-8aea-d78673f38e3e | -3.3687 | -59.427 | 2026-09-10 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 51c7553a-693b-376d-8b34-97ef920cf4f7 | -8.9522 | -44.9731 | 2026-09-10 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 9cf12a0a-c124-30c1-b150-f6766fff8532 | -7.5195 | -45.0064 | 2026-09-10 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| fce44c53-ad7b-3343-afc0-c4c67111bc53 | -9.7141 | -43.3956 | 2026-09-10 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 248b8a1a-69fa-3b21-ba26-81714ec2f361 | -8.6311 | -66.5287 | 2026-09-10 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| c7dfd60a-4074-3bc8-a9aa-24e61dd43132 | -6.5453 | -62.8914 | 2026-09-10 14:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| f31968bc-3fa2-3992-ac33-95bc6ca0c0aa | -9.7702 | -43.4589 | 2026-09-10 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 4559c9d9-2d15-3151-9efb-1dedc273f4b4 | -10.7585 | -45.917 | 2026-09-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 58cb6ba8-71d4-3660-86ce-21db4c8a8703 | -9.6947 | -43.4217 | 2026-09-10 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 253.1 |
| 38f29b9c-512e-3dc0-91ba-7fde11d6443a | -6.7864 | -58.8801 | 2026-09-10 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| df20d300-d73b-3d7d-8b2e-50c07ae3fad3 | -9.7698 | -43.4825 | 2026-09-10 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| fdebf610-ba5d-3eb6-b198-24e0ba1bcc34 | -8.7253 | -62.4177 | 2026-09-10 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d32e2251-7b72-3c7b-9b78-013e6bff6a18 | -13.228 | -61.8131 | 2026-09-10 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 31ee3ddd-00bf-3f8f-ae08-9af29fbdbe65 | -8.9412 | -44.3995 | 2026-09-10 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1fe0cf79-1e2b-3539-b4f7-112d2945b357 | -11.4026 | -43.935 | 2026-09-10 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 220.6 |
| f423d6e9-4bf8-39b2-81f2-513d205c26b7 | -13.2284 | -61.7743 | 2026-09-10 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 513f9488-6455-3486-98a5-98ebbef86db5 | -7.587 | -45.6804 | 2026-09-10 14:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 965e2557-570b-3fdb-b52a-1088e705259c | -6.7695 | -58.6097 | 2026-09-10 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 5e5a26ef-890f-3216-8f6b-4cea8fdaee98 | -13.2092 | -61.795 | 2026-09-10 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 149b0cf2-1032-310a-b0a9-e5321f1545e0 | -13.2667 | -61.7329 | 2026-09-10 14:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1f591545-4185-3169-9d91-70edf18fe26e | -8.6012 | -47.347 | 2026-09-10 14:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 67c46b70-1cdf-3df1-9a9f-9a030bfee106 | -9.6944 | -43.4453 | 2026-09-10 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 129.1 |
| 42dafe72-8998-313a-ac5c-00f1ad0e5ba2 | -6.5452 | -62.9102 | 2026-09-10 14:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 482a1ade-748a-3e2b-8cea-f4afa5fb05bb | -7.9834 | -43.9951 | 2026-09-10 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 244.8 |
| 439a3d19-be93-33a1-ae84-6cb9ff4e0feb | -9.7933 | -47.0449 | 2026-09-10 14:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 2ecd232e-8bbd-337b-b8db-2d531b998031 | -6.641 | -58.4987 | 2026-09-10 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1b9fc53a-104b-3738-a280-a83fff39a438 | -8.9708 | -44.9939 | 2026-09-10 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1e38c48d-8979-3b19-8548-c5e96000c889 | -13.2282 | -61.7937 | 2026-09-10 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| aa1de59e-1f1a-34cf-bd22-2cb6edcfced2 | -10.7582 | -45.9397 | 2026-09-10 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 9110faa8-8306-373d-b0b6-320759b34245 | -8.7254 | -62.3987 | 2026-09-10 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| dbd0d50c-addc-309b-bef7-5306b2cb566c | -6.7648 | -59.4408 | 2026-09-10 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6f6f81b9-03dd-3967-b95a-19bde1836d60 | -7.5195 | -45.0064 | 2026-09-10 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 783ff9db-34ad-3e19-80a1-a1dd0d4fbb61 | -10.7398 | -45.8967 | 2026-09-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 04747e81-75b3-3e03-94f7-2e7af2917fb9 | -7.4976 | -45.2814 | 2026-09-10 15:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 46908d8d-1a67-3338-8b7b-836b3a5aa3a9 | -3.1462 | -60.6506 | 2026-09-10 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 0d033d42-6238-3f58-951c-f187c87841d2 | -13.2289 | -61.7161 | 2026-09-10 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3d7ade09-5442-3944-b318-44a84352f638 | -13.2481 | -61.6954 | 2026-09-10 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 45369f67-caa6-3aa8-b7f2-4da9748e3a5e | -13.2092 | -61.795 | 2026-09-10 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e9174cdf-1175-3114-909a-00690e08f980 | -6.5004 | -47.5909 | 2026-09-10 15:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| cd77c82e-a583-39a9-93f4-9ac7b612039b | -10.2556 | -45.2521 | 2026-09-10 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 162.2 |
| b8f9f3f9-016c-33e7-93ca-b65ada6ea16a | -15.6142 | -56.3898 | 2026-09-10 15:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 46006636-e690-3275-9ed8-1e66dffa39e1 | -13.2293 | -61.6772 | 2026-09-10 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fe5b0669-64e9-3e07-b397-899083d6884e | -9.7698 | -43.4825 | 2026-09-10 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 165ef598-ab95-316d-b41f-413c9ac2673e | -10.2552 | -45.2751 | 2026-09-10 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 70abb4e4-e194-3b92-888b-201075b9368c | -6.5637 | -62.8908 | 2026-09-10 15:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7496129c-bac5-3274-b727-6ebbce88b659 | -8.9712 | -44.971 | 2026-09-10 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 19f944aa-2304-3549-9f4d-4a3178e20901 | -13.3298 | -61.1064 | 2026-09-10 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 681f53e6-79e0-3b48-a3dd-1e536a1d475d | -7.5167 | -45.2569 | 2026-09-10 15:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 05d18b41-353f-3386-b131-728b40854578 | -8.9522 | -44.9731 | 2026-09-10 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| f9cae0ee-4628-32ba-be30-74732e6fa4c1 | -8.6311 | -66.5101 | 2026-09-10 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 03e4e868-bc69-3816-ae6c-95dc7296c0c2 | -6.7695 | -58.6097 | 2026-09-10 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| dc9382cb-ae4f-3773-8c11-fc6a8971e7b4 | -10.7582 | -45.9397 | 2026-09-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| b2c5744c-befc-3112-b0fd-eb5010319fdf | -13.2667 | -61.7329 | 2026-09-10 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5e6cc53f-3bd4-3091-8e12-3aef2ffe97ab | -6.5453 | -62.8914 | 2026-09-10 15:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| f26f0aa7-46b1-32e2-8e54-689d9f213e2e | -13.2297 | -61.6384 | 2026-09-10 15:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| dd7fcf2a-f342-3533-a1f6-73c838aa4882 | -6.5452 | -62.9102 | 2026-09-10 15:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 807ee81d-30f8-38e5-80f9-687482a6ede3 | -10.2358 | -45.3004 | 2026-09-10 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0ec8f262-0275-3cee-9293-f98dd6cca413 | -10.7395 | -45.9194 | 2026-09-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| f5e5bd50-ceae-32ea-b420-1caef51b98d0 | -3.4028 | -60.3232 | 2026-09-10 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| c3dd6da7-ace4-32f0-a359-37f07bbc91e1 | -9.006 | -65.4 | 2026-09-10 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 3b6fd48b-1dd5-3b6a-8e4d-0be5e4aa2a59 | -10.2746 | -45.2497 | 2026-09-10 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f5399ae9-dce9-34c0-bb8a-1ba1c31b052a | -11.4026 | -43.935 | 2026-09-10 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 60a02ea4-7225-3389-8c3d-fe95c27f27c6 | -10.2362 | -45.2775 | 2026-09-10 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| dd377cd4-23ff-3845-987d-ef694a267602 | -2.7332 | -57.6077 | 2026-09-10 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |


[Clique aqui para ver as próximas entradas](README51.md)
