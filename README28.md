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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bafbaf6a-ec9a-3b2e-9b83-c2df0104aeca | -15.05114 | -43.84035 | 2025-08-25 04:17:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3122257b-c2ff-341c-b8b6-9b0325dfbc0e | -13.80983 | -45.88425 | 2025-08-25 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 581d7bc2-8ad2-3e96-a5cb-354b1c376f37 | -21.12963 | -48.91842 | 2025-08-25 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af9cb648-17e4-31a9-a445-eb545f82cbeb | -22.60168 | -46.03695 | 2025-08-25 04:17:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9b6959cf-ed1e-36fb-8573-607c96819055 | -13.47541 | -47.01283 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7cdb5b3-500e-3b23-976c-14e683d82fc9 | -13.65743 | -47.98328 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41c3950e-5a86-34b2-a866-1828f47b6bfa | -12.49196 | -53.82711 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9e4506a-c339-39cf-8001-50fb10a79c59 | -13.00708 | -56.88822 | 2025-08-25 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27e78207-338e-3826-a829-83f75a4a4c40 | -12.68781 | -47.82917 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70486670-b5f1-39c2-8e10-3a0833700745 | -12.75517 | -48.11739 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ec4b888-6a89-3061-8033-8ac1a765731d | -11.20029 | -48.46942 | 2025-08-25 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc211ee3-4b4d-37f1-870b-55a44d851c82 | -11.27475 | -44.98773 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49c1b41a-b2f7-3919-aa35-f7e1f50c8eb0 | -21.13238 | -48.9231 | 2025-08-25 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 42b8d22a-edfd-3d13-8d94-27060cd1f04b | -12.75876 | -48.11823 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 147c241c-b6e5-3730-b446-3e07134accb2 | -12.93748 | -46.30924 | 2025-08-25 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 16a346d2-f696-3551-89a9-47306b2bda93 | -9.71266 | -54.99147 | 2025-08-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2e3dfde-20a2-3c92-91ba-b5546cfb5b5e | -14.34139 | -51.96357 | 2025-08-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ddf20e4-1cb1-3b86-b20d-ac00ed3ff3da | -14.2581 | -48.0395 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2c04a21-237d-38fb-a0e2-7607b8e6698a | -14.43548 | -56.47502 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88425c0b-dde5-3626-b8b0-29b4b23a2305 | -13.44965 | -46.91404 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f341ae9-d519-36a6-a50e-b139684cce83 | -15.07246 | -48.67874 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5daba6d4-55ba-377a-b504-b4f6057f4d31 | -12.17936 | -47.20075 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5eea2c22-7129-328d-a0df-7dc43997d2ce | -17.50021 | -44.78743 | 2025-08-25 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50b1e5c4-c818-398a-90ae-59e97aaf90ee | -20.36219 | -46.72257 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35905654-c86f-3432-93ef-1138a7b7225a | -13.21614 | -43.15167 | 2025-08-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4881133c-5ef9-3823-8958-cdcdfcc01ea3 | -13.00661 | -50.55519 | 2025-08-25 04:17:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c11e98e-2e06-317f-9a67-0281dd46930c | -13.45167 | -46.88015 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d7e3ea5-8164-33b3-bc77-a684ed869786 | -11.28525 | -44.98581 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f41087b-a614-31ae-9da2-919ddec02669 | -20.45642 | -47.4133 | 2025-08-25 04:17:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 74e1ce7b-3d5a-3f30-8659-a12d1b6c4023 | -12.74411 | -48.1383 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c336895-6170-3767-851c-3a35b0c3e5b4 | -10.02447 | -51.07468 | 2025-08-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e093146a-6956-3377-a8a3-010694486d02 | -21.16136 | -42.91078 | 2025-08-25 04:17:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 06c38d01-7b1a-37a4-b3a9-9fa7e6e296e0 | -10.02011 | -51.07003 | 2025-08-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e0492d-04bf-3bdf-926e-fb66c306a1f8 | -15.17564 | -48.20334 | 2025-08-25 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57792456-8397-399f-acf5-bd69e8f67c97 | -20.36334 | -46.71526 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2f1bd03d-71fe-3a60-a858-f8c3ab5c6590 | -16.50329 | -46.74393 | 2025-08-25 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e82f703-9cd2-30b1-835c-6180bb76a918 | -10.88535 | -55.78887 | 2025-08-25 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8f38d393-6eac-3b65-80f4-0736faa1c5f8 | -11.63769 | -46.21942 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07884e97-d6fa-3f87-ae97-43703025662f | -20.6192 | -45.02785 | 2025-08-25 04:17:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| fa800438-5f32-33fb-ab83-fe6b8d8a3123 | -10.61266 | -55.04638 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9b3e2f1-a178-3616-837b-466d5d452033 | -11.64231 | -46.21248 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9df586eb-5325-3152-90c0-de6b1f2e2844 | -10.59943 | -44.32857 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9f698e62-a4b4-3ee7-8f04-ac5157e2de33 | -10.7687 | -47.07891 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a2b500d-8f47-3ce5-932c-1408a61ab57e | -12.18636 | -47.20194 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c178cc93-5e2f-3f47-a97d-d710eee30a64 | -13.05695 | -46.32938 | 2025-08-25 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f2fb419-378e-3d79-8990-f789b5150bf3 | -13.50954 | -46.91311 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a1d2800-8694-3c31-9fb2-6ecb06dc664b | -15.05169 | -43.83665 | 2025-08-25 04:17:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b6ce12df-ab8f-3ab9-8877-db14de3c66ab | -20.35169 | -46.72416 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88183ec0-1651-3c05-87f5-46a4d3d9a1c3 | -11.09526 | -44.7678 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 683dc8bd-3297-3c27-9e47-104fa83c98fb | -14.10945 | -53.99644 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 07280306-d93f-341f-a3a6-60d48bf08dd5 | -13.04043 | -45.24529 | 2025-08-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95400832-789b-347a-b234-90d89eb03af7 | -14.74283 | -55.92854 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8737287a-57c5-37a5-aa2b-42eeadd634d6 | -11.09913 | -44.76482 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9237ba8c-ce12-3c60-98c6-d85bda04d6fe | -11.10572 | -44.7875 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b6ab7a0-0a37-3a21-a143-52c3d6b05961 | -16.31062 | -48.89405 | 2025-08-25 04:17:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7720e8d-a103-36f5-88d9-d7c607a62bd8 | -12.99247 | -45.22653 | 2025-08-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d9011fc-c748-3829-b16e-6e6bea0a0e27 | -12.75134 | -48.1398 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 747ed8d6-0b5d-3a94-8b2a-43f7958d0b08 | -13.81259 | -45.88839 | 2025-08-25 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 491ed949-c90b-34da-b63b-c0206979f6a3 | -10.77292 | -47.07539 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f1f0fa-62d6-34a7-b6f7-2707fbfbbf43 | -23.43143 | -47.57769 | 2025-08-25 04:17:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 428e72eb-4378-3053-8f4b-6776db19c122 | -10.02842 | -51.07624 | 2025-08-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d998b1d7-3945-3bd0-bd02-638b009ab742 | -15.64581 | -52.7265 | 2025-08-25 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bdd294a-5f39-3696-bf75-5614982c6a34 | -11.06707 | -44.60094 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d84acb1c-98f5-3827-b52f-290a94682438 | -13.28956 | -47.51491 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b594a381-359a-30a5-825e-96332bbd9c69 | -20.37407 | -46.75486 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2340c98a-af87-345c-88c3-1a3dc2844535 | -12.75955 | -48.11362 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f0a1d461-2d4f-337d-9c6a-d45242d9c478 | -11.1264 | -49.98695 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2efea21-d390-3537-b182-ccd53758d0ef | -11.26642 | -44.97556 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 819974e1-34ee-3a20-b28f-66f4f4d93a07 | -21.63149 | -44.0224 | 2025-08-25 04:17:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d2137432-e44c-3746-addf-739de9c462bb | -22.68811 | -47.35136 | 2025-08-25 04:17:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0335160b-8582-3c3d-b937-e5eea1285988 | -10.76938 | -47.0748 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8185b97f-e501-3781-9475-354b3f3dbf15 | -21.96687 | -45.76328 | 2025-08-25 04:17:00 | NOAA-21 | SILVIANÓPOLIS | MINAS GERAIS | Brasil | 3167400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1c82526e-b0cb-39fd-b1cf-c9f0465d401a | -13.43253 | -46.91114 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2062dbef-cee1-32a1-bf62-fc495986a1a1 | -20.383 | -46.74137 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58bd0d2d-303b-3a03-a73d-d56e5af74302 | -13.00079 | -56.88703 | 2025-08-25 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a1b881-f31f-37fd-8ee3-99f3c41a87a3 | -15.0834 | -48.65861 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5109d2b0-48f1-3a78-ba6a-61ca136a06f8 | -13.45105 | -46.88399 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 756cca26-2c14-3688-89c2-2d713249f0d4 | -14.23877 | -58.62116 | 2025-08-25 04:17:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9cd17a7-ac44-37f7-b515-7d734b38070b | -11.6417 | -46.21619 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 337b8678-bb41-3150-8d70-3427bacd262c | -11.14382 | -44.73967 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2425a0c1-354f-3567-84f3-86187204158d | -15.04942 | -43.82872 | 2025-08-25 04:17:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d6705864-3eb5-32aa-ac1c-afd09f219bcb | -12.753 | -48.10822 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6c5c657-ac64-3c95-9b7c-96c91bb10987 | -21.63236 | -44.01566 | 2025-08-25 04:17:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| a4efbbd6-014a-3234-bc2b-0c2963dcabde | -13.34223 | -54.38976 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67075158-c93d-3ef1-b970-9c0205ddb7b8 | -11.47216 | -55.47746 | 2025-08-25 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad388a55-e62c-3e5d-8cd8-5650fe068c95 | -16.23557 | -48.1478 | 2025-08-25 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 955eaf77-24d7-3d43-8e4d-a6fd00af7446 | -20.34367 | -46.60228 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85a9991e-a6b5-31fc-a07a-702b99088131 | -10.62491 | -51.62072 | 2025-08-25 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70ba3bf7-4969-3485-9733-437cc4879815 | -12.6914 | -47.82978 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e6bfde9-649c-3fe0-95f6-8752e51f480a | -19.93969 | -47.48996 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 401c2b1e-2a5b-3597-bc8e-2e7539b9aa45 | -13.43402 | -46.92355 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 859153eb-108f-3328-aadf-2684737e6d9b | -20.36277 | -46.71891 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f1f34492-72bb-3dad-b0ea-109e95879e46 | -11.27138 | -44.98723 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 984dea83-8e82-3edd-a0fd-d9fdbafdfd4c | -11.86937 | -45.12141 | 2025-08-25 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc437044-7dcf-36ec-aee8-847724ff3f3e | -13.39064 | -51.80527 | 2025-08-25 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3215b6ab-4c0f-39be-81b0-65142d871b51 | -11.10847 | -44.79154 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 430f142f-aeb6-3d63-bce9-ba402491923c | -11.20109 | -48.4647 | 2025-08-25 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9fd1bdad-4bd8-35ee-9adb-9a04dc908df8 | -20.90488 | -44.08244 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b05a3af5-4d79-323f-a68d-83e4d1552759 | -15.62653 | -52.70273 | 2025-08-25 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 803c13b4-023a-36d8-8464-19be4b19bd8a | -13.50739 | -46.90482 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README29.md)
