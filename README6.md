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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4064528-28e8-37ee-8556-b49c5ac5052f | -9.67412 | -49.71373 | 2025-05-03 12:36:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 20cd4079-a996-30b9-9434-bc0a6701029c | -7.4987 | -49.2473 | 2025-05-03 12:36:00 | TERRA_M-T | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 53160a90-e377-3f87-ad2c-09009deb8a10 | -9.67283 | -49.72263 | 2025-05-03 12:36:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ee542474-b720-33f6-b333-407d6ae71365 | -10.01648 | -46.58615 | 2025-05-03 12:36:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 87852dc6-b965-3bcd-9410-039a4c50c999 | -16.428 | -43.47331 | 2025-05-03 12:38:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| bafb92c4-5677-3b59-a9ea-873450be3967 | -13.71183 | -45.1918 | 2025-05-03 12:38:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 9e9339aa-da38-3cf0-9e3a-3b0961c66f45 | -13.7003 | -45.19036 | 2025-05-03 12:38:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| df0b8836-dd05-30e9-b2b7-ee85591b0b40 | -17.20948 | -49.85692 | 2025-05-03 12:38:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6a5e86c-f2c5-36a6-81f5-5ae7e6856a9a | -13.70984 | -45.208 | 2025-05-03 12:38:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| cbe935d7-0480-3ba0-abd1-c339712f8c2b | -11.39501 | -52.93671 | 2025-05-03 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cf947ab7-371d-3008-b491-6e4beb0be3e7 | -13.69832 | -45.20663 | 2025-05-03 12:38:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 9ef7bb84-9528-3a32-ae23-1a5b4300234e | -13.7075 | -45.1988 | 2025-05-03 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 96657db8-4ff2-301e-afb8-1adfc28e9f6f | -18.26443 | -53.01176 | 2025-05-03 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c99000e5-9ff8-310f-a681-f7236f053703 | -18.26292 | -53.02169 | 2025-05-03 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6119002b-5e43-3fd6-9c28-e00c3b8b7c2f | -19.57921 | -48.6741 | 2025-05-03 12:40:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cd453329-dd1f-3555-a047-fd75e51d506a | -19.98636 | -47.18835 | 2025-05-03 12:40:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ecafbb92-fe43-37dc-885f-b7a859f3a678 | -17.62364 | -50.91377 | 2025-05-03 12:40:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c38bbc62-4009-3987-b7ae-71246913a379 | -21.89622 | -49.04548 | 2025-05-03 12:42:00 | TERRA_M-T | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 136f3457-e2a4-385d-a139-ad3c12aea65a | -22.67539 | -49.80744 | 2025-05-03 12:42:00 | TERRA_M-T | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e481c16e-08b9-3eba-9425-1662116331eb | -29.71282 | -51.28579 | 2025-05-03 12:44:00 | TERRA_M-T | CAPELA DE SANTANA | RIO GRANDE DO SUL | Brasil | 4304689 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| ac5b5e28-ee62-3e06-920c-00300fc0699e | -29.79939 | -51.64042 | 2025-05-03 12:44:00 | TERRA_M-T | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| 785db60f-c191-3f85-9974-306c6a202534 | -29.72242 | -51.28732 | 2025-05-03 12:44:00 | TERRA_M-T | CAPELA DE SANTANA | RIO GRANDE DO SUL | Brasil | 4304689 | 43 | 33 | nan | nan | nan | Pampa | 26.1 |
| b84beef4-a4b9-3222-b45a-1655bfa7cb36 | -13.7075 | -45.1988 | 2025-05-03 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 116f85d2-7c15-3335-8e19-84cd505d2326 | -13.7075 | -45.1988 | 2025-05-03 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f78e8721-73e3-3fa5-871d-8d76f36dbc23 | -13.7075 | -45.1988 | 2025-05-03 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 5ed3d45e-7610-3727-a358-64fef58f7da8 | -13.7075 | -45.1988 | 2025-05-03 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 4942d72e-f3f3-3d52-8e7f-f608c8fbdcc2 | -13.7075 | -45.1988 | 2025-05-03 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 60a13d75-962d-3b4b-b426-1031946798cf | -13.7075 | -45.1988 | 2025-05-03 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| a06e6552-8f5c-3315-b6b3-0214e898f9c5 | -18.2632 | -53.0312 | 2025-05-03 14:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |
| e4bb1871-ab6c-3f5b-b533-5c002245c7e8 | -18.2636 | -53.0096 | 2025-05-03 14:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a62ce177-aa88-3711-90b0-a3a1f6a83dc7 | -18.2636 | -53.0096 | 2025-05-03 14:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 851affc3-463b-3ee5-96d5-915a87fcf885 | -18.2632 | -53.0312 | 2025-05-03 14:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 171.0 |
| eda8ae9b-7b2c-3630-99b5-1d1123a6eb6b | -18.2632 | -53.0312 | 2025-05-03 14:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 91115fa8-b42a-3523-b2f7-bb5fe7ab6f86 | -18.2636 | -53.0096 | 2025-05-03 14:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 181ea815-2e65-30cf-a47d-e1b21f30fd97 | -18.2632 | -53.0312 | 2025-05-03 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 206.7 |
| a33e9175-bacd-3f0b-b870-331726d05a85 | -18.2636 | -53.0096 | 2025-05-03 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 22db3526-1b44-3181-986f-0d17ccd603a9 | -18.2632 | -53.0312 | 2025-05-03 14:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 156.1 |
| e0e0ece9-e560-31b7-a35f-5ec59f63f43e | -18.2636 | -53.0096 | 2025-05-03 14:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |


