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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 037b1b1a-b596-3fbf-965e-fabeb4361801 | -20.7223 | -49.4471 | 2026-07-28 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 21829ea0-d601-3884-931c-b96a4a1b6bba | -17.3034 | -42.6678 | 2026-07-28 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4e0e68fc-98c8-36ff-b6ac-e7bdae84ad4d | -11.7691 | -47.0685 | 2026-07-28 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| f085ba3f-78bb-307b-aa3f-e99b99161293 | -10.3822 | -49.5849 | 2026-07-28 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 2c513f86-a29b-3c26-b32e-f373f86e152c | -11.7879 | -47.0884 | 2026-07-28 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| d4b1f8ae-6cf5-3f91-863a-bfe8e3dfba33 | -10.4011 | -49.5829 | 2026-07-28 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b8ec9dba-565d-341f-8efe-304c1c83a790 | -12.8543 | -44.386 | 2026-07-28 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 224.2 |
| ad0eabae-156f-3210-b85e-15e35e992e51 | -14.2688 | -58.9853 | 2026-07-28 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 3ff8b2cb-45bf-37a7-bd61-8c6b859b68aa | -13.3032 | -45.1045 | 2026-07-28 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 90a19693-ddeb-35a7-82cf-603204c73824 | -17.3235 | -42.663 | 2026-07-28 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b06a8ec7-b123-368b-b2bd-a0928818f643 | -14.2882 | -58.9638 | 2026-07-28 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 0b5d38e7-113f-311d-bcbc-ce241b2c25ad | -20.7435 | -49.4197 | 2026-07-28 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 118.0 |
| d35b8d2e-dcca-3c86-aee3-93443c30971e | -12.8349 | -44.3892 | 2026-07-28 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| ca665de9-275e-3b94-864f-9a2fc7862dbf | -10.3825 | -49.5634 | 2026-07-28 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 87e145a4-dd45-3b83-b93f-7a20c6d14932 | -14.2691 | -58.9654 | 2026-07-28 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 8e5d679a-2311-3464-9b00-23c6a713be1d | -12.8354 | -44.3657 | 2026-07-28 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 3a60e173-ee10-38c6-85ab-88e487b0427f | -18.8004 | -51.2417 | 2026-07-28 00:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ec214b04-f046-336b-882f-a94fa522cd3d | -14.288 | -58.9837 | 2026-07-28 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| fa586bb8-dac9-3d1d-b671-dddce6661f69 | -20.7429 | -49.4427 | 2026-07-28 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ce41fd91-0232-3ee3-9b4f-01cbc2ef23f2 | -13.3028 | -45.1278 | 2026-07-28 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 67236e89-de30-3cd3-b502-97404a92a46b | -12.8548 | -44.3625 | 2026-07-28 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 954dd641-39fb-390d-8467-4a6c4dcccae1 | -17.3034 | -42.6678 | 2026-07-28 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 003a8800-0413-3dc7-b179-ba211ecc269e | -12.8548 | -44.3625 | 2026-07-28 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 7e741e88-cf43-31d7-ace9-e9e533d24a41 | -10.3825 | -49.5634 | 2026-07-28 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c7c9bc59-375d-3d47-b557-2c810410ca24 | -20.723 | -49.4242 | 2026-07-28 00:30:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 196.8 |
| f214b598-8670-3a2c-af97-183cddc15cd8 | -14.2882 | -58.9638 | 2026-07-28 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 174.6 |
| ac66b420-836d-354a-a867-70cb7283cd32 | -10.3822 | -49.5849 | 2026-07-28 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3d45e908-ebc9-3c90-9b8d-8e4ac15ccfe6 | -14.288 | -58.9837 | 2026-07-28 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6e6bcaad-40ea-3c12-bc53-765c479ef22e | -17.3235 | -42.663 | 2026-07-28 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 116.9 |
| acaf09bd-fed9-354d-97a7-31ed5a12bba5 | -10.9397 | -43.0593 | 2026-07-28 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| b10cdb5c-6372-3792-980a-e5fb618cd901 | -9.4 | -40.3722 | 2026-07-28 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 3d7fdb96-fd24-31ca-9fda-8f1da2496f29 | -20.7435 | -49.4197 | 2026-07-28 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 53.7 |
| cc0888e9-caa5-3c46-9d4c-64edbd0a28d5 | -20.7223 | -49.4471 | 2026-07-28 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 9559d4c2-fa7b-3e82-a1d1-e1a5426a5a1a | -14.2691 | -58.9654 | 2026-07-28 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 8f464f1b-5286-3acf-96c4-918094a5b32e | -4.3774 | -47.7627 | 2026-07-28 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 1e45200e-bcf4-37c4-bcd8-cd3f5052389a | -17.3228 | -42.6878 | 2026-07-28 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 33aa1daa-7383-3d9b-9f1e-53b43f95be84 | -14.2688 | -58.9853 | 2026-07-28 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 753b2db5-2000-3fc1-9d81-1f212d68a753 | -13.3032 | -45.1045 | 2026-07-28 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 8f676663-81c4-3307-80a1-dbb056ed1644 | -13.3028 | -45.1278 | 2026-07-28 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 308b720c-5291-3d1f-94dc-b1b39599c498 | -12.8354 | -44.3657 | 2026-07-28 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 34a7f553-f39d-384a-a284-09dca9efb77d | -12.8349 | -44.3892 | 2026-07-28 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 84273bca-d883-3c79-8cab-5855b2e9a9f0 | -12.8543 | -44.386 | 2026-07-28 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 207.0 |
| ea9be6bf-adeb-339f-8bba-8a38f665f3c6 | -18.14845 | -52.7922 | 2026-07-28 00:33:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 838dd0b9-dcde-30ef-9bbc-ed591c29474e | -20.61958 | -57.26737 | 2026-07-28 00:33:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8210b966-b6cb-322c-9fc4-6ea37275c479 | -22.0681 | -56.52854 | 2026-07-28 00:33:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e2eda084-fc06-3377-a42a-fe0041797b03 | -18.1499 | -52.80202 | 2026-07-28 00:33:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7af9bd19-8ed8-39f6-b4da-5523ff371eb2 | -22.05834 | -56.5299 | 2026-07-28 00:33:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 172c09b3-cc22-3539-8287-1afdd59b80cc | -23.97973 | -48.5241 | 2026-07-28 00:33:00 | TERRA_M-M | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| ff88d515-f221-3b69-beae-5e4891bdad96 | -20.62959 | -57.26597 | 2026-07-28 00:33:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 308241e2-5af0-3fdb-82df-d6d9be95b045 | -18.80394 | -51.24845 | 2026-07-28 00:33:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 54093e05-2c28-3d61-8e97-5c48071fd7c8 | -20.61814 | -57.25525 | 2026-07-28 00:33:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8abfd49f-d1e4-3753-8a0a-e96dc5845177 | -20.72076 | -49.4262 | 2026-07-28 00:33:00 | TERRA_M-M | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 057db607-8711-3480-9d9b-01df046cc5fb | -14.30093 | -58.97248 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ecf6e474-5586-3593-b42c-dd6c8e858588 | -12.46814 | -50.53639 | 2026-07-28 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e611b7ef-4f0a-3277-b54a-5b5b274fd78a | -7.41548 | -46.82993 | 2026-07-28 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 9c7b7f82-aaa7-331c-8390-931e6c3f1daa | -16.72613 | -49.41846 | 2026-07-28 00:35:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8de52843-f6be-3e59-8b56-eb56150403d1 | -7.41097 | -46.83798 | 2026-07-28 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ff0d1827-24d1-3542-8081-5091f5416232 | -14.24548 | -59.01122 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 099a5d87-7694-32c0-94d2-59f117932e45 | -14.27319 | -58.98186 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b92a0bc6-727f-3620-9283-dc6d356ea5e1 | -9.11002 | -56.86401 | 2026-07-28 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7782899d-f7b3-3d40-8215-94cb20df3271 | -14.2629 | -58.98319 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 5cf10ce7-896d-3f66-9db1-8708cd2e780f | -12.3239 | -46.74625 | 2026-07-28 00:35:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| f7cdaf3c-90f9-3da1-9e31-19356769da67 | -14.30248 | -58.98521 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2be9eee8-7785-3214-93c8-65ef33d54182 | -14.28034 | -58.97512 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 8830453f-ec70-3ac3-8313-395e0135c798 | -13.2999 | -45.11067 | 2026-07-28 00:35:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 56987ac9-e96a-3468-81c0-b3b9ebba8221 | -14.26856 | -58.96397 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 4c19db08-22d8-3997-8f14-ac27e45925d7 | -14.40174 | -58.87678 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4de8afaa-bc29-34c2-8348-23611808a613 | -14.2716 | -58.96935 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 38204fca-5e65-3cdb-bd60-fc4db0384bcd | -14.2305 | -58.97478 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3a451430-1162-3d40-b157-c04edf7d95ef | -14.23204 | -58.98726 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d576909a-eceb-3c76-a54c-186b998819ba | -16.45877 | -48.99562 | 2026-07-28 00:35:00 | TERRA_M-M | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d051802f-a0b3-3e0a-aeda-e4e508880b47 | -12.47955 | -50.53447 | 2026-07-28 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 39132221-ee4f-3dc2-95c9-02f8e132bd28 | -14.27006 | -58.9765 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 88557e0b-0271-3a1f-9dad-755ab15d371e | -13.70704 | -51.90071 | 2026-07-28 00:35:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5b58715d-e4db-3291-ad58-1552912726e9 | -9.11764 | -56.85381 | 2026-07-28 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 02be88b8-5ec0-3c99-bcc6-fdfbdc963b07 | -15.24176 | -48.58734 | 2026-07-28 00:35:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 1f686305-0e46-3ad5-9ba1-645d51a5e682 | -14.24232 | -58.98588 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 940b54c1-14fe-3167-a51e-3a166a1a6bf8 | -13.30715 | -45.1502 | 2026-07-28 00:35:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 12e2b7db-1d03-3996-a001-188235b2f9b9 | -10.38058 | -49.58645 | 2026-07-28 00:35:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 66852aa1-b321-3883-8b4f-db798c569579 | -13.29716 | -45.11622 | 2026-07-28 00:35:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 198.4 |
| dfe1bf91-3921-3c1c-a39c-6e0cb95731ff | -14.26133 | -58.97071 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 5d437a1d-1e41-3466-a541-965977ee28a2 | -9.47693 | -57.32189 | 2026-07-28 00:35:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a7da985-2f39-3bcd-8e1d-424afee8a7c2 | -14.27884 | -58.96259 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 55b0c9c6-46e4-3818-9830-1971da7c8546 | -14.29063 | -58.97376 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 17847900-19ce-3c33-a0c5-7f2e2c418b3e | -12.45165 | -46.51757 | 2026-07-28 00:35:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| eaadd9f4-4f4a-33ef-bfab-2e9a3c9d5faf | -15.24199 | -48.58044 | 2026-07-28 00:35:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| e3fb2a34-6e29-3a00-b0f6-46d95d9ea9df | -10.39338 | -49.58433 | 2026-07-28 00:35:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| b4138e26-77ad-3215-9afc-5ddef44d535b | -10.37732 | -49.56632 | 2026-07-28 00:35:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 75894539-0768-3c91-8d0a-4754073f1120 | -16.72883 | -49.43472 | 2026-07-28 00:35:00 | TERRA_M-M | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 23c6c5a1-958d-3a8a-9a14-f9d3498361af | -14.42219 | -58.87405 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1fa35235-f222-32f8-9308-0bf4900a0509 | -7.46005 | -49.72636 | 2026-07-28 00:35:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| ae9debbc-fd50-369d-bd06-42e4b45dbf95 | -13.35879 | -54.28763 | 2026-07-28 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7f78d8f2-967f-387f-b468-d1ef7b7a973e | -14.29216 | -58.98641 | 2026-07-28 00:35:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 090c1275-3170-3386-8959-e0211feecd39 | -9.10879 | -56.85507 | 2026-07-28 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 026fca19-bffe-3f2a-812b-b5091f3bdd92 | -12.47063 | -50.55201 | 2026-07-28 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f11694f3-8337-38e6-a255-4ccbb359f60e | -16.86847 | -49.58118 | 2026-07-28 00:35:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3671539c-a016-3ef1-8208-e2a20fd23a35 | -4.36439 | -47.77553 | 2026-07-28 00:37:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 21ba53f6-0870-3397-ba1f-7abb4a4ce290 | -1.51169 | -54.54145 | 2026-07-28 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5c92c4c3-53c5-38c8-9d72-16fe3684555a | -1.67539 | -54.46918 | 2026-07-28 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cabc91e1-3d69-3293-be6a-c69273db3472 | -1.52012 | -54.53427 | 2026-07-28 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README4.md)
