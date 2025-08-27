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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9aecaf7-691f-3f42-8d33-fa2b858ed496 | -12.775 | -48.12006 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3236ba51-d80e-3427-a0b8-e702d5a73eab | -12.71419 | -48.13911 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 604dac99-96d3-39cb-88c8-78f54aadf833 | -11.82713 | -46.80233 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1c7181e-3327-3629-8fa8-04860d73d4ae | -12.76786 | -48.10078 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9adf682a-895f-3fb8-9a43-86287ee31d36 | -13.35271 | -54.39138 | 2025-08-27 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27ea2a98-4a5f-3d7f-818c-546b1c02579c | -14.32747 | -53.2626 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89d27bd3-1b21-30cf-aad1-7235b78a5315 | -12.95317 | -44.58446 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 378b960f-9302-302d-a5c7-3f68a176543d | -12.75715 | -48.18971 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5796def0-2144-3ad9-a337-7a9a0cd336b3 | -15.11408 | -48.55394 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b1c69a1-18c7-38fb-9132-8996f5343985 | -17.78706 | -44.49712 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95e0f955-914f-3ea6-99b8-16abd04be1db | -9.4089 | -60.5422 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4f4bd867-e926-39e6-9431-af2156d56482 | -15.12243 | -48.67253 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41799de5-6ff8-3e88-bcbe-180971cdb322 | -12.42676 | -45.96693 | 2025-08-27 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbd5ba0d-d483-375a-8626-4e847fcf5665 | -15.08912 | -48.62681 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6200d3bf-b37d-3f93-9994-358567efae35 | -12.74883 | -48.19925 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40464787-6a21-3d70-9b12-2d80e56f2d0f | -13.39421 | -46.91817 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e32ebba-2ab8-304a-9f7c-0279170db09e | -12.80248 | -48.11726 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 744f5f42-0c12-3053-8cd9-9db5f42061de | -15.52182 | -47.3932 | 2025-08-27 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 761f344b-747d-34a0-bad2-90ade9831d58 | -15.63645 | -52.73821 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5780681e-30f5-39f3-88d8-d0ab492c6847 | -15.10388 | -48.61811 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99f4e9c5-73a9-3e63-a20d-c1e23bf3bf3e | -13.38753 | -46.91708 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7728e3f8-01b8-3810-bde0-390bc7d5cdca | -13.42588 | -46.86024 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bd353aa9-73c6-35a4-815a-5f4da33661b6 | -12.56948 | -43.78832 | 2025-08-27 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 575d48bd-492f-36cc-91b2-0c5d93664e76 | -12.5702 | -43.78603 | 2025-08-27 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1e6b150-4830-3e11-a71c-8a4e874e14af | -17.17546 | -48.68177 | 2025-08-27 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 274bf0d4-db24-3fc3-b48a-17cb34cf1274 | -13.60665 | -48.14423 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5763b877-d1fd-327a-b51a-b740a33eb138 | -13.49111 | -46.85958 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4d0a6b5-1c92-3ba8-9a5c-d94ce142f25f | -12.40749 | -46.48951 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef1d09f1-81b6-350e-a679-a96a3f6de0fd | -13.44498 | -46.98166 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c565925-e72b-32fb-9d97-fc600ac5dcd9 | -12.76546 | -48.18018 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f29008e2-6fa3-3111-a596-addedc94f4e2 | -12.76455 | -48.10023 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f72aa93-0d9e-3f34-a50c-0f87b65cbe29 | -13.35191 | -54.39566 | 2025-08-27 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4274518-323f-349b-9a8a-0189896c54b5 | -12.76328 | -48.17251 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18dc0ab2-1be1-3419-bc85-77b7d2bc9df0 | -13.23073 | -46.54681 | 2025-08-27 04:27:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad0c718f-fa29-3899-8363-2e6a5250ffe1 | -15.60959 | -52.74062 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 299827ff-6d0f-37d2-a5ac-3a639401c062 | -17.54957 | -46.62166 | 2025-08-27 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d612d091-f21b-3cbe-96c6-a36902a4adf8 | -13.82612 | -45.89337 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65d52c6a-3a62-366b-a0b9-ae2bbb87d109 | -13.06301 | -46.33735 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8bb7a41a-a1c5-368f-a49f-eab6d2d0c949 | -15.6432 | -52.74445 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0d2a004-99df-3317-8e9c-50aaaad00646 | -13.18122 | -44.04388 | 2025-08-27 04:27:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebffc263-ca2e-357e-b499-c248335f5d71 | -12.41139 | -46.48643 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d0b39ce-1fac-3c28-b115-e1968d20c1b5 | -10.41154 | -57.70937 | 2025-08-27 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 317f4ad5-8efc-3d8d-83cd-6a080e9cde6b | -14.76567 | -59.73084 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 81a5cd8d-9d71-348f-ac1b-204532cbab02 | -12.74389 | -48.18753 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 468bd173-55b5-3b50-b32b-fbeb7cdd11ab | -12.24835 | -45.05836 | 2025-08-27 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a67fadab-41e0-3bb5-b407-c5ffa7afe48f | -19.05947 | -41.9099 | 2025-08-27 04:27:00 | NOAA-20 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 94d4d707-aca1-3655-bac5-8bf6e719aebe | -18.69262 | -47.79691 | 2025-08-27 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d47e21b3-7eb3-3ec4-a29c-9a8e7aae1191 | -14.52399 | -53.02696 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb7b8482-1e04-33be-91a7-c9396768ec89 | -14.50673 | -53.16968 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b938fd11-fe41-3537-b1f3-6e3f70a226bc | -15.66392 | -52.7384 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90c9a50c-fb73-3bed-8f43-7ee6358d3d1b | -11.79471 | -51.4058 | 2025-08-27 04:27:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a10762ae-918a-3bca-a90c-d975bc2bee7c | -12.78881 | -48.11871 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b43f60aa-ef26-3387-aea3-f9cdb376ac61 | -13.43276 | -46.99444 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13ec9ce0-f133-3a36-8b67-437451f58a1a | -12.8003 | -48.10963 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe8fb0a9-d179-3b57-a6c0-24533cc921bf | -15.78836 | -43.34821 | 2025-08-27 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f809e918-8b09-3367-82ca-66e0513b1bed | -14.8418 | -49.21483 | 2025-08-27 04:27:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de573118-2051-39d1-b0b4-99b49a139392 | -15.09677 | -48.72679 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a328025-8ba7-37a6-9bf9-a3945556b4b4 | -15.53428 | -54.74848 | 2025-08-27 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c59be3a-80d5-32c4-b9b2-76c538099046 | -15.62212 | -52.73043 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf636607-273e-3330-8ca0-90be3cf72e60 | -19.2345 | -48.8184 | 2025-08-27 04:27:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6129f6bf-3eaf-3c57-8144-b7236f3efbc7 | -13.425 | -47.00046 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d379618-b078-332b-85a1-dd9fa677e4ff | -13.42667 | -47.01185 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdead467-5aea-3793-823d-71c305b39c96 | -18.28897 | -40.99464 | 2025-08-27 04:27:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 48f40e57-e0cb-3eeb-8ad5-86f492d82d92 | -11.03283 | -52.02859 | 2025-08-27 04:27:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ec0318b-a67c-318a-99c9-257139cc2bf5 | -12.74085 | -48.07829 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a31a7aa4-a4d1-31c5-b569-3b5f3d91d85d | -16.60372 | -40.99051 | 2025-08-27 04:27:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66c02767-059b-3632-8181-399a464bfccc | -11.9142 | -46.74686 | 2025-08-27 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38a28e57-2318-3ae4-815d-3785a60cd35a | -17.17215 | -48.68121 | 2025-08-27 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa5f7e0e-a3be-3c9e-8d3f-05c3d7ef718b | -12.78493 | -48.12171 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d3ad0b7-aade-33ca-8a94-4fcdfe5001c2 | -13.39031 | -46.92122 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a8178cf-510b-36cc-a860-abe04959a09b | -12.75354 | -48.08398 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5126c521-10f1-3662-9a06-48d1290e72a6 | -12.78825 | -48.12226 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 770eba78-d550-3b91-b58a-fadd043040f7 | -19.24646 | -42.05061 | 2025-08-27 04:27:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 301ef951-3bf3-3dfc-a326-9737fc7178ea | -14.7668 | -59.72543 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 052704a4-9054-3217-90f1-fce2e82a281c | -13.62361 | -48.20873 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a22ccf63-20cd-3d73-a77e-5b71a9366d7c | -13.42444 | -47.00407 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a36a1a1-aacb-3c06-8ebc-7331178153e9 | -18.15359 | -44.43818 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 856bf6f9-ee9f-3a83-8de3-b37872ceef4c | -17.01079 | -47.94987 | 2025-08-27 04:27:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be938a10-ff13-383e-840f-b1ed7acf9b12 | -17.77592 | -44.47993 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81fc9f7f-2974-3a68-9d10-463cd4d713b3 | -9.39903 | -60.51989 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92b3cb84-2957-3fd3-8c92-010045698378 | -13.17194 | -45.28514 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a50a9b0-97bc-31be-abce-5aff5d61ba2a | -13.42613 | -47.01539 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22a043a0-1b35-3738-b74e-3be9d0d4a6a2 | -13.39087 | -46.91763 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 043a9589-19d2-3bce-a3b9-44bb2f1cb624 | -17.78319 | -44.49659 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84c3f935-e2d1-38e5-bc3d-8ee04d9a3ae6 | -14.76777 | -59.72079 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1887835-bd09-3c0a-86b2-badf1a3cf27c | -12.74277 | -48.19461 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91a21e80-199c-3964-b5d4-cd62ddb0e98d | -13.62305 | -48.21227 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daaf8c72-cecb-3a75-b0b6-b6f38a919ce3 | -13.06526 | -46.32264 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 027356a7-d0e9-399f-838e-9d2e7fcadfd9 | -14.36405 | -53.3588 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ffd0a21-c0fa-3f1d-a665-598634b607fd | -12.76322 | -48.19438 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c0b36c6-f085-3b7d-8789-cdec34870518 | -17.31499 | -46.59916 | 2025-08-27 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a3f7f91-f27c-3872-bc55-3ca5e8f7255a | -13.35654 | -54.39443 | 2025-08-27 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fac1c64-3b87-3192-9e21-88d88395fc21 | -9.40072 | -60.54726 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 25d02232-17f8-3950-a8dd-31e09f6e7ae5 | -19.25102 | -42.05162 | 2025-08-27 04:27:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a1530dec-dd2d-32b1-9bc9-57922d362995 | -13.06748 | -46.30809 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25d84a3a-1bdd-38ee-b1f1-5df1e02be264 | -9.40459 | -60.52791 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 95af7a30-3214-3a02-ae2f-cc03a410775c | -13.39865 | -46.91153 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a463c85-bb4c-3edc-ac12-de6fa9b1b3d3 | -15.03642 | -48.68018 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f880af4-c0a9-3f31-bf7f-e394f44a4a85 | -13.61918 | -48.21527 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09502c52-1c94-3a01-b70a-6c6519eebcb4 | -16.77921 | -47.56007 | 2025-08-27 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README46.md)
