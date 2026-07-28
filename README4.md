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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2146a5aa-b029-3421-a621-baf91d02a0dd | -4.37018 | -47.76948 | 2026-07-28 00:37:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 707acc91-39c2-316c-b3f0-11fc5c84a7cd | -12.4681 | -50.535702 | 2026-07-28 00:39:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e585329-7d4d-3710-9f60-9b49fe941636 | -12.851 | -44.378201 | 2026-07-28 00:39:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1aab7dc8-d673-326e-8a9f-b485805e52d3 | -9.6081 | -47.7673 | 2026-07-28 00:39:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9894c20a-b5e5-34c3-8dc3-0e1ba47c8495 | -7.6727 | -47.1945 | 2026-07-28 00:39:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab489f3b-dd44-3e59-9fbf-14e72122c574 | -11.771 | -47.077099 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ba41e71-25ce-35ad-bad1-c7e91fb32b4a | -10.3831 | -49.578701 | 2026-07-28 00:39:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0eea6d78-85f8-3a5a-8a8d-b800652849e1 | -4.3675 | -47.758598 | 2026-07-28 00:39:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af45109-b4b9-3efa-836e-46b48838395c | -18.153799 | -52.799599 | 2026-07-28 00:39:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1e47026b-fc18-319c-8248-6c8f695db00f | -13.3013 | -45.110699 | 2026-07-28 00:39:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0799e837-9530-3cff-a60e-5014b5604009 | -11.988 | -45.547401 | 2026-07-28 00:39:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6b61b59-535a-32e0-ac01-3f8f7f176598 | -6.8687 | -45.994099 | 2026-07-28 00:39:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86cbfe24-b91e-37b0-a350-98a4f703b9a8 | -9.6065 | -47.760399 | 2026-07-28 00:39:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9684343e-4632-3ffd-91b7-580a6464122d | -12.3228 | -46.737099 | 2026-07-28 00:39:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb2f801-fd84-3995-9a13-fe8f136dd15c | -15.8123 | -41.889801 | 2026-07-28 00:39:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9597425-3b77-393d-8820-143b8b430e0a | -12.4886 | -43.7649 | 2026-07-28 00:39:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| acda9b1b-6204-3c63-a9d5-18eef62ab33a | -11.7808 | -47.074902 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd259b4f-8cb2-3a85-a071-8f5078f96ae4 | -7.2457 | -43.137699 | 2026-07-28 00:39:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1fa8f572-314a-3ff3-b7c0-de1063694f88 | -12.8431 | -44.3885 | 2026-07-28 00:39:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53a6634e-eab5-3236-8e38-8f9610c7bca6 | -20.720699 | -49.4263 | 2026-07-28 00:39:00 | METOP-C | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dc1dff83-136d-36bd-b51d-64231d4d6216 | -12.3244 | -46.743999 | 2026-07-28 00:39:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95accfab-4c72-30bf-889b-d3abdec770c4 | -3.6798 | -49.4851 | 2026-07-28 00:39:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 636fb23b-5203-35f1-a3ea-cacda08238eb | -15.4436 | -41.360699 | 2026-07-28 00:39:00 | METOP-C | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f59b9d0b-b4d3-33fe-9f81-9a0d382bb6a9 | -5.488 | -45.120399 | 2026-07-28 00:39:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e004244c-58a9-34d4-9a1c-36cebb5fc5de | -6.8723 | -46.0093 | 2026-07-28 00:39:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b76e1418-158f-3f22-a89d-50c2251c2a49 | -12.4984 | -43.762501 | 2026-07-28 00:39:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8dec33-c026-3d01-819e-71a52aa8fe85 | -16.455999 | -48.996799 | 2026-07-28 00:39:00 | METOP-C | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d35f6f89-156d-391e-a262-278bd2f8ee70 | -12.4906 | -43.773399 | 2026-07-28 00:39:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6623f00-841d-3166-9376-be582b881fb4 | -14.2609 | -58.981499 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 561086af-255c-3729-be6f-13346a00e2ff | -9.4109 | -40.3554 | 2026-07-28 00:39:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5ce3635a-49e8-382a-aed1-04d9942b1614 | -12.4584 | -50.5378 | 2026-07-28 00:39:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e264dacb-c3ca-36ea-bc28-e419569655d3 | -9.3394 | -47.9006 | 2026-07-28 00:39:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b157889-66c5-3764-8083-d5bddfc69e16 | -11.7792 | -47.067902 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab85b5ad-7db8-3d16-9ff9-47404b79991e | -9.3673 | -44.718498 | 2026-07-28 00:39:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a96efd83-595b-357e-946f-1a408acfc227 | -4.0558 | -43.243698 | 2026-07-28 00:39:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9521dfff-5a6a-3308-8674-f355df33ffc4 | -12.8529 | -44.386101 | 2026-07-28 00:39:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d043a538-46fd-3eb1-9b7b-9f9f85a6dae7 | -7.6743 | -47.2015 | 2026-07-28 00:39:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be1fefb0-f3d9-3a61-9e69-3cdccfbce482 | -18.803101 | -51.243198 | 2026-07-28 00:39:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 31f7acf9-7132-3b99-b0c2-b4d1a276c2d1 | -6.1914 | -47.302299 | 2026-07-28 00:39:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8ea57b2-c386-3ef9-a486-7f9421bedc86 | -10.3733 | -49.580799 | 2026-07-28 00:39:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e85233b-e58f-38c1-b0a0-f852617960a7 | -12.8492 | -44.3703 | 2026-07-28 00:39:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 205632d2-b827-3bbd-83d2-a705ca9c8b04 | -14.284 | -58.9436 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbbd4ab7-88d0-3cad-84e2-fb2facdfcbe5 | -3.6782 | -49.478298 | 2026-07-28 00:39:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84801455-9f70-391a-9ab1-b1ce08d7e09b | -1.5101 | -54.5326 | 2026-07-28 00:39:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2b5a48f-7047-31ea-bf28-6f8a4ad2c422 | -16.457701 | -49.005001 | 2026-07-28 00:39:00 | METOP-C | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4cb66c0-9a84-39d0-b71f-32866b8efa6a | -17.307199 | -42.674702 | 2026-07-28 00:39:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d1368a31-6f8b-3ab6-903b-4ee6929b1da1 | -12.4779 | -50.5336 | 2026-07-28 00:39:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dffcc3b3-cce7-3b90-8355-40fcab26484f | -10.9458 | -43.065102 | 2026-07-28 00:39:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee14cd6a-4165-3b2e-b532-7d39dee23161 | -14.301 | -45.6408 | 2026-07-28 00:39:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df2214c7-c5e5-38ca-b7e5-45830ae9823b | -7.364 | -48.143902 | 2026-07-28 00:39:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22c09d70-0a73-3eff-a953-ed5e1d82afa9 | -17.315001 | -42.663601 | 2026-07-28 00:39:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c4228da6-46ce-3942-898b-cf415a8f3f40 | -15.4488 | -41.381802 | 2026-07-28 00:39:00 | METOP-C | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1de3930e-a0b8-34c1-835d-5d1a01e92d84 | -7.7147 | -46.526501 | 2026-07-28 00:39:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d1356af-31e2-3110-b111-826b03e5fcbe | -12.8548 | -44.394001 | 2026-07-28 00:39:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c30c0e23-c4fc-31df-887e-3c5daff2b1ff | -4.3707 | -47.772598 | 2026-07-28 00:39:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85682722-4812-3a29-b8d2-3501c2adac10 | -9.405 | -40.372898 | 2026-07-28 00:39:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b427e7e0-654b-3351-ba3a-65b0e27aebe5 | -14.2744 | -58.945301 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66cbd616-d10e-3169-8d1b-de84e89baf5f | -10.3848 | -49.586201 | 2026-07-28 00:39:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc87d85-89a8-3f25-91af-ce13e10857a2 | -7.0142 | -45.424301 | 2026-07-28 00:39:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 713d9b3d-a5ed-3c54-8f9d-a9387c6fe4da | -12.845 | -44.3964 | 2026-07-28 00:39:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42c98205-4cbb-3e73-910b-c1e0d2028478 | -10.9435 | -43.0555 | 2026-07-28 00:39:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9fc4401-19e3-39e4-862a-c0bd38c50a62 | -10.9412 | -43.045898 | 2026-07-28 00:39:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e22c491a-917d-36d0-9aed-3677e2d9609c | -5.8235 | -43.486198 | 2026-07-28 00:39:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd1af7e5-cd86-3275-879f-8bbfd38172a7 | -7.8991 | -48.2761 | 2026-07-28 00:39:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7351376a-e892-3c2f-b43d-d4b6cc39b916 | -17.3962 | -47.335201 | 2026-07-28 00:39:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 060fb470-facf-3890-8260-d47144cb126f | -14.3026 | -45.647999 | 2026-07-28 00:39:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54a5b90d-0075-3fdb-9c6d-f071e8caada9 | -10.3717 | -49.573299 | 2026-07-28 00:39:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6876891-e37e-379d-9472-b333520ba873 | -7.415 | -46.8372 | 2026-07-28 00:39:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc2ccd55-a308-3c23-b2d1-06121e941e4f | -15.2389 | -48.574699 | 2026-07-28 00:39:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ef1b64f-da47-3d0a-b7fc-8c267ba8b6f9 | -13.2996 | -45.103298 | 2026-07-28 00:39:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f986f483-02f5-3683-a81e-859a82e5a77b | -11.7725 | -47.084099 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99a76be5-4410-370f-9e50-0715b6fa4593 | -9.4147 | -40.370399 | 2026-07-28 00:39:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4e46750b-0615-345c-a160-cf28e5d15f1f | -7.0123 | -45.416302 | 2026-07-28 00:39:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e245caf5-4914-391e-85e0-205b7b1a860c | -7.0161 | -45.432301 | 2026-07-28 00:39:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbc6f67-30d9-3f2e-b511-eb6247b3b25c | -12.4593 | -46.521198 | 2026-07-28 00:39:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29c590a2-24bd-3b7c-a89e-83d17a04d7ea | -14.2706 | -58.979801 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 321a2302-9b9f-3a11-b9c6-0773087fc2dd | -9.9263 | -47.898701 | 2026-07-28 00:39:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e41a481-d8ac-3724-862b-5f02fe6cae8f | -9.4087 | -40.387901 | 2026-07-28 00:39:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d097333b-d28f-37fc-8dc2-cf589995e318 | -10.3815 | -49.571201 | 2026-07-28 00:39:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92416164-972a-3aa7-b6bf-aa25436e1878 | -5.4266 | -43.421101 | 2026-07-28 00:39:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d9dc9dc-456c-3fef-befc-8813de0d8eec | -11.7823 | -47.081799 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebec5287-5a04-3e8f-9cb1-d07d6517f8db | -6.8705 | -46.001701 | 2026-07-28 00:39:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db7b668b-f09d-3211-8cd4-18605b47790d | -23.978701 | -48.526299 | 2026-07-28 00:39:00 | METOP-C | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f2dcdbce-935f-3bc5-833b-103df8b3c621 | -9.5268 | -47.1381 | 2026-07-28 00:39:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d58b8ca0-f23f-310f-b81c-40d98bb84b1c | -5.826 | -43.496799 | 2026-07-28 00:39:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35233c74-e161-3797-8742-7fed9cc2d51f | -12.4561 | -46.507198 | 2026-07-28 00:39:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76ca82f5-5828-3112-8d00-71182e0a3fad | -4.9423 | -48.241299 | 2026-07-28 00:39:00 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43cc93e5-70fb-3cc5-a624-cb7a92f518e5 | -12.4798 | -50.542301 | 2026-07-28 00:39:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab9dadd-2257-3709-ad25-b1297cdd0d06 | -11.7921 | -47.079601 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b836ef2-1acb-3e02-b7c9-a13c7b4ed031 | -17.319099 | -42.680801 | 2026-07-28 00:39:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9f42828b-05ee-31f4-aa81-0290717c47d5 | -6.193 | -47.309299 | 2026-07-28 00:39:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01d9167b-e404-3404-9915-a60dee033630 | -15.4462 | -41.371201 | 2026-07-28 00:39:00 | METOP-C | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0114c5b2-2fdf-308b-94ae-a58dbad92e5d | -18.8053 | -51.255001 | 2026-07-28 00:39:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| adac56be-9f8b-3096-970a-44e6779b1dd2 | -14.2648 | -58.946999 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94730c93-1e0d-3944-b4a0-d430c702f32f | -10.7522 | -42.099602 | 2026-07-28 00:39:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0ec268e5-1a34-37b1-a7e9-f2c22bcb21ce | -15.2405 | -48.5825 | 2026-07-28 00:39:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 608bfaf9-3ea6-3fab-9be5-fbba25dbc0bc | -10.7592 | -42.086102 | 2026-07-28 00:39:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4f66e3af-2c51-37b8-83cf-7864138e3d9b | -14.2802 | -58.978199 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc654eda-e54f-3821-9a24-9c9e2b2c8f06 | -20.7246 | -49.445999 | 2026-07-28 00:39:00 | METOP-C | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4684b599-5fd0-3b4a-b874-aeff809ba02a | -18.856899 | -43.452999 | 2026-07-28 00:39:00 | METOP-C | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README5.md)
