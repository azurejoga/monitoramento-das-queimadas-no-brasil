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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6da196ca-c2e8-3d39-90a6-9daefe0cbd3c | -11.43184 | -44.94138 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f03e4091-661c-3cc8-ad41-a2c40c4ebc8c | -13.84223 | -45.62479 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd14271d-1011-3f1d-9380-3004dab6ab30 | -12.86369 | -44.69223 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fb74eb4-bcd8-385e-a3dc-be9b516d6e84 | -12.41394 | -44.75067 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91affdf0-ad55-3d8b-9f07-4d9999dbc272 | -11.69949 | -44.39764 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 070babd4-7ad8-3ffb-b1d3-6bc89dba8b09 | -13.83602 | -45.62817 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e57eb518-cac3-3df3-b8dc-9b2ed84cb20a | -11.78594 | -45.57189 | 2025-09-25 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2d39178-3dba-3c93-9130-8e501f15da82 | -12.05735 | -44.83112 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49e79e3d-6941-3080-b588-b86cecb099ae | -13.84176 | -45.62886 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35f17ceb-8ca4-3682-ac30-73b6ddbc1754 | -10.5943 | -44.08643 | 2025-09-25 05:01:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e805e17-8a0d-33de-b497-f2c9125a5d60 | -11.03927 | -45.88394 | 2025-09-25 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea7ab3f1-137b-369e-b6ac-f0c116e92d8e | -10.59137 | -44.06925 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcb07ec8-5906-3764-ad0a-046683c06858 | -11.67426 | -44.40365 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5274f16c-f228-3e9b-8e37-be1f4f3f65ed | -12.54 | -45.79961 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8eff424-9cff-3b3b-9812-fcc92cd25109 | -13.83649 | -45.62412 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce9e873d-df93-3b85-a569-0116edb49dc3 | -10.53755 | -48.59119 | 2025-09-25 05:01:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5ce72fc-fa33-33ad-a0c2-cbd79b8d9e95 | -8.50406 | -44.99784 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aab9a97-6f7f-3cb8-8a79-e6ac59ce74aa | -12.8642 | -44.68773 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f2e059e-094c-3b4b-a705-c9df808b65f9 | -12.53955 | -45.80336 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a6fb8e2-a57e-3a8e-b960-5d08d8c44895 | -10.59579 | -44.08385 | 2025-09-25 05:01:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dcb6b01-3721-31da-afdb-af1a711ce3a3 | -12.84869 | -44.69587 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc1e2631-3b53-3515-8d64-fa12c170813a | -7.76979 | -46.1913 | 2025-09-25 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11308d5b-73dc-38a8-ac11-3f251e0d5961 | -11.03884 | -45.88729 | 2025-09-25 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 507311b5-7180-3bdb-ad4d-6b678fe9a36d | -11.4275 | -44.93581 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 299ad64f-d22e-3217-8dbe-a0a0758eb3d9 | -8.73227 | -45.42079 | 2025-09-25 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b6b21de-ed33-3825-a3b5-af2ac4264927 | -11.80314 | -45.5709 | 2025-09-25 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4314c26-bac0-3c48-b71a-9c15b1ed72ae | -10.39197 | -46.1721 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a6997b4c-48cc-3214-af9e-dee505f1eff4 | -12.84268 | -44.69512 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd03fa50-e9ff-3543-a225-051221dd57ab | -11.43242 | -44.94362 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 736b5b1a-fc07-3531-a8e6-9bbac8784cc9 | -9.43793 | -45.59169 | 2025-09-25 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6feef472-4b18-3665-9b4f-90004533a76b | -12.05147 | -44.83017 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16693b89-e2d5-3221-b484-b906ee41887c | -10.40083 | -46.18649 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 366ff2bc-09d9-370f-9eef-b37272a12499 | -12.54045 | -45.79587 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4d5d5da-eb1a-3f38-8aba-a34f34e10b0d | -11.68852 | -44.38709 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a7ccd2b-2591-3a92-b55d-9bc02c1a3be4 | -13.83696 | -45.62006 | 2025-09-25 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db47b43d-5151-34c5-932a-910e95381ad2 | -11.41049 | -44.97752 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e870a16a-5fc4-3634-99f9-aa1d8926361b | -10.39768 | -46.1696 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30892bac-b498-36ee-bfae-b6a026a8845f | -12.5391 | -45.80713 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 338adebd-d424-39db-98da-56c4fb32f822 | -10.59027 | -44.07849 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15da023f-bbb1-357f-8123-b549a112c6d8 | -10.58447 | -44.06656 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e044b0b-5a34-3ef4-a660-3bb4f15e58fb | -8.51056 | -44.99155 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff349e91-07c2-33df-86f3-a5163fcd02b7 | -12.8514 | -44.67336 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 551f63ec-c024-3293-b011-27e2544d652d | -11.68742 | -44.39612 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9d9be39-2c66-3df5-a8dd-040bda87084b | -10.58584 | -44.06387 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6173e38-1b0f-34e8-ba5e-f7f3916086d2 | -10.58939 | -44.07651 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53ab8103-c726-3b53-8da6-440af4e37534 | -10.40125 | -46.1833 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f62d9c1-208d-38e3-843b-f89bdbbb0d3c | -11.78889 | -45.56833 | 2025-09-25 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5a7983d-762e-3fb0-80f5-5b5b4d161dcd | -11.6748 | -44.39914 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2647586-801c-392a-84cb-f44d739619c0 | -11.69346 | -44.39688 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9aeb36e-8329-3d8b-8869-bd9244584cfc | -10.09481 | -46.32307 | 2025-09-25 05:01:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 028a501c-4642-3764-b8aa-550cd3b66bf5 | -8.5101 | -44.99501 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 152e7cd4-8ec3-3547-9b93-0d06e6c36055 | -11.42703 | -44.93959 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74426a2d-493b-30c1-97c4-4362497e97a3 | -12.06748 | -44.84626 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb5ca69f-749a-3fc4-a044-55f8993ba3c7 | -11.42656 | -44.94334 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d7bf279-2a26-3072-bb1b-bf5945968166 | -10.38605 | -46.13498 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8768f8d4-f6f7-343f-afba-f2b3fa9761d9 | -11.04388 | -45.89112 | 2025-09-25 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eeffad8f-7a9e-383a-8fc2-2c9c1c81428f | -9.43838 | -45.58834 | 2025-09-25 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0eeaed98-088a-35b1-8ca6-527700b3abca | -10.3924 | -46.16882 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc8b8a66-2f62-3a2a-b33e-9e2687dddb48 | -12.84485 | -44.67706 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c07d989-3148-3146-bd7b-acc3df3edf61 | -10.28455 | -45.22788 | 2025-09-25 05:01:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb46ead8-5138-3208-852e-4de0e294989e | -8.4906 | -45.01399 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20eb1a40-d683-33c0-905c-5ea5c5d49d35 | -8.28636 | -44.95181 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8139ad8a-60a3-38e9-8ddd-379b2966acf4 | -8.49758 | -45.00399 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50153b36-35b3-3e0f-90e2-a64a28cff16e | -7.77153 | -46.19102 | 2025-09-25 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73cfd0b0-b8a7-3b54-97aa-2998b7ad285e | -11.04302 | -45.89798 | 2025-09-25 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e8cbc9a6-0725-37cc-90df-97151d56345f | -11.90942 | -44.77981 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b510d45-fd1b-32f4-9643-282427c1363a | -8.29193 | -44.95256 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e56816c-99db-354b-ad52-e65bf4d61003 | -12.84666 | -45.29781 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eb8e0af-f357-3571-9e00-6d6ef1dc113e | -8.73816 | -45.4182 | 2025-09-25 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8daa224-04d4-30f5-b23a-b2015a054bdb | -10.09564 | -46.32341 | 2025-09-25 05:01:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c872ea2d-3cde-307a-8474-432052246050 | -11.68906 | -44.38258 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ff84ba3-b764-33d4-ac98-7df73aed27d3 | -11.7805 | -44.87838 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea1960b1-d0e2-34ab-9c67-daab3d0166a7 | -8.28144 | -44.94612 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fef6e984-b974-384e-a7f2-7cba2eb29735 | -8.28813 | -46.01549 | 2025-09-25 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e313947-c55a-3709-846d-0786bd924da3 | -10.59056 | -44.06727 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 308413aa-6a66-33d5-b1b6-320407aefc1c | -8.48638 | -45.00311 | 2025-09-25 05:01:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 757cfb61-469a-3e45-9908-19eaaac3f1fc | -10.58881 | -44.0811 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 928faf07-a919-3f69-9ed9-10b489d931e6 | -11.62348 | -44.31414 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c80c5d7-2e97-3232-a9ff-52ef85d6cac6 | -10.10877 | -45.32732 | 2025-09-25 05:01:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aa59e99-2841-3004-88e0-f06144ddd349 | -10.59192 | -44.06463 | 2025-09-25 05:01:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 050e8537-1ed8-35f5-9a75-adffa5b6aaba | -10.38563 | -46.13822 | 2025-09-25 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b741687-2e9f-36a5-bb8b-4cd5b9fcbe19 | -10.11049 | -45.32851 | 2025-09-25 05:01:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71811f19-46a5-33ff-a667-4e0703348a82 | -12.85368 | -44.67292 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bec579c4-d419-3db9-84af-965da57e1d7a | -11.91043 | -44.77122 | 2025-09-25 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1db5c7c0-14b7-3641-9a01-0ad6c0ab692a | -11.43138 | -44.94532 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2caa3b2d-d8cc-3dac-bc8a-ebf4446c4dd7 | -12.84924 | -44.69132 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91a53338-888a-3a65-93dd-38c1aa7b85ee | -11.64034 | -45.35484 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e43423f1-fc0e-3eae-a5f9-8ea51485c691 | -12.41447 | -44.74629 | 2025-09-25 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbbdb368-ba0d-3ac7-a133-a4a316467e9b | -11.41743 | -44.96916 | 2025-09-25 05:01:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56d3effd-54ec-3b1b-ba08-628358d38d73 | -11.62018 | -44.44699 | 2025-09-25 05:01:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5deb17b8-a827-379f-bd7b-c91fb8c6016a | -20.98763 | -50.47607 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 72f52fa6-5847-36a9-a032-30fa80ae79e1 | -15.7687 | -59.47982 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e94d137-d113-3e4a-bbfa-ddd0ada2f1f9 | -18.26036 | -51.13092 | 2025-09-25 05:04:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97d2cc93-52cd-3f56-acc5-cccb97d0a6d4 | -15.36437 | -59.178 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6678eab4-5c35-3400-870c-cf53e46eb2ef | -20.70373 | -56.74566 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63decd4b-69c9-3be2-998a-f520facb1e6f | -15.89986 | -59.34461 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 38ede19f-8009-351a-9aba-14e7acf4ec84 | -20.69917 | -57.86139 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c2a691f2-573f-34d6-93a1-d925fde10e2d | -17.92665 | -55.86874 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e351ccfb-0152-3b78-96de-a242ef5ffc65 | -15.90698 | -59.34604 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 127937ad-7cdc-3785-b4cb-58588ea08699 | -16.85331 | -50.51752 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README31.md)
