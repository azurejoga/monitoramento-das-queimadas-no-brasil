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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34eb602-3495-3b4c-9834-9cdd0b2b2472 | -8.23074 | -55.28268 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a45035-c431-3f87-8379-5218356a7680 | -10.82706 | -51.09238 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b3b1ea4-0985-328e-a419-58407913ed99 | -12.5363 | -43.08905 | 2026-10-02 04:59:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5ce432b5-d6e5-379e-bf64-2666e6f1fd93 | -11.78925 | -43.56117 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 230fc1fd-3cb0-35e5-b3e7-7f9043b81d11 | -11.68122 | -43.60047 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97e50356-c4ce-31af-b74e-6b807f5a18d7 | -11.46835 | -43.4392 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3d9b768c-4161-3048-8ba8-78753421dd90 | -11.73775 | -43.44487 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e1812ff-3e14-3229-ab27-744a6392d286 | -15.63624 | -43.23695 | 2026-10-02 04:59:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4c88dc3e-a959-30a7-b6e1-7dd06b4ca7fd | -11.42501 | -43.40408 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e64e44c5-38d9-3e4d-8437-db33b5a2bdcb | -10.32262 | -45.36226 | 2026-10-02 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2226b069-71e6-3659-bf99-6df47902017e | -12.66725 | -45.09524 | 2026-10-02 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbdb7817-7bef-38fd-8d87-f1bc72e0817a | -8.30051 | -54.72561 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04cd2cc6-01f5-3d99-927d-fdee9dcd1f6c | -10.56338 | -49.95784 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6acdf0b-c44a-34f6-ab5e-ff7556418552 | -11.77374 | -43.58282 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b271f527-16b6-3cd1-817f-3a3306780ce6 | -11.25526 | -45.22825 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc9afc3-ee1f-3ca3-8c2c-b7fad415cf44 | -11.18553 | -58.15778 | 2026-10-02 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61e7f8a7-66b8-3f23-bb46-e46be4ce74e4 | -8.29721 | -54.72508 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76994cc9-6243-31e0-b89a-44d80f682fad | -10.5757 | -50.08036 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af520f32-b457-3e6c-9ee3-a111d9a8926d | -11.64532 | -43.55385 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c50d186a-6687-39b5-913e-de273dce6c87 | -11.80282 | -43.57338 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49ac225b-80c3-3918-95e3-60e624b0930c | -8.91948 | -55.16516 | 2026-10-02 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c64d53e-3a06-37c2-899a-4c1f768beca0 | -11.74217 | -43.57605 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 48cf4019-9eff-3cbf-bb67-2753d665150b | -9.74417 | -53.89556 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d30d34-d41f-396c-b4b9-3afbf266e442 | -11.783 | -43.57692 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 816fd83d-4bf9-3a8b-a226-079586a5cd77 | -13.86123 | -43.63516 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 983eedc6-558e-35e2-b12c-d41f2abc2a8c | -9.82165 | -44.81356 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a65e169b-f5d8-37aa-8486-52d8d6b479cd | -9.33672 | -50.99685 | 2026-10-02 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15885278-39e5-3e92-aff2-4f550270a1b4 | -11.73194 | -43.43865 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaa6bbc4-1564-31ed-a2b4-7131831a4b10 | -15.50937 | -46.1228 | 2026-10-02 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5312a086-b9d4-34b0-b172-ebf30a437351 | -9.76555 | -53.7993 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 558a48ac-a899-3838-8505-0e8dddfc3df2 | -9.81983 | -44.83824 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14a3deb4-fe2e-3ce7-af2a-51de22fe9df7 | -11.79698 | -43.56772 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e96c6350-cb2a-3edf-ab15-f4d8c0ccf5fd | -8.27855 | -54.73635 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84de5aa6-09f5-3674-ba18-bede448be133 | -11.14252 | -44.59956 | 2026-10-02 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 10666524-5672-3a85-b413-189a2a550d13 | -15.30815 | -42.78724 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 44f76cd6-0359-3fca-9f4a-0982600a7328 | -10.81488 | -51.0955 | 2026-10-02 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0470d73c-771b-3988-9eea-9ad82d8682ac | -10.39652 | -53.81388 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25ba775d-ecde-37a6-a602-020eff9d5dfd | -9.66552 | -47.66366 | 2026-10-02 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94107fd8-550c-3646-82be-5da9fbb13778 | -11.74142 | -43.58258 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 11776a6e-85a9-3e2d-9e7a-70fee798553d | -11.73255 | -43.43322 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7588db9-0004-3287-8174-02cf7f14c89d | -10.26364 | -49.65757 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 475a0a78-28b7-3d37-ba3a-c2dba4a603a2 | -12.19041 | -57.11208 | 2026-10-02 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c463b466-e9fc-360e-ba20-edb115365fc8 | -9.84277 | -44.84183 | 2026-10-02 04:59:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d2c6ac8-0e0e-398d-ab50-76efbfbf0462 | -8.59255 | -53.11062 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77373edd-b535-3c92-bfa2-0ca29366b1c1 | -12.52968 | -43.08815 | 2026-10-02 04:59:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7ced414c-9f7b-3f45-8491-a4ea49f3a539 | -11.2656 | -43.51361 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbbf006d-79d3-3d21-bd6e-8872ffbac3ed | -11.46805 | -43.42593 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ff73ef7-f55d-36f1-924f-7fe33e60da42 | -8.31221 | -54.76295 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ff50878-8089-3002-9ee7-f4c49fab58c7 | -11.24182 | -45.19605 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f430422d-af6a-322f-958f-9dbbe3d52038 | -8.4187 | -54.70876 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af58db0f-ba4b-31bc-b271-5ba834262a3c | -11.26497 | -43.51884 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7961f5ce-a5ed-337f-bb59-5174639aa878 | -9.58109 | -54.62915 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a87b39e6-ad44-3312-b253-35678693db79 | -11.46678 | -43.43667 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b2d3129-356f-3748-b894-dc4f89a91fa6 | -8.54382 | -54.56128 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcc0b5d9-c274-3d86-880a-546fb8cee6a7 | -8.53944 | -54.5677 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a555c55-21a4-3898-bd49-b5fad317f1f8 | -8.5047 | -54.94633 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 031e25d4-346f-3480-bd44-202870436094 | -10.41387 | -53.76803 | 2026-10-02 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c4a2e6f-ade6-339f-8c67-ca2d4ed112f6 | -15.32283 | -42.7803 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a65b507f-6926-30a3-95d5-5b31270e9b28 | -15.25434 | -46.17359 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 628de21e-e7ce-3c4a-bfe2-a051caf4821c | -13.86036 | -43.64088 | 2026-10-02 04:59:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bd127962-be9b-3672-80ef-d46c8dcef66b | -11.66156 | -43.6031 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6e388b5e-af82-313b-b3f9-9165763c9eed | -10.9422 | -68.72565 | 2026-10-02 04:59:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 56fe89bf-38d1-3ed9-8bb3-263ba2be4145 | -11.67146 | -43.60649 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef97da9b-9880-3e1e-bd69-3ef89fef1e79 | -8.30541 | -54.71577 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2560cc88-2a8f-3981-890d-3c6ffaac34dd | -11.77606 | -43.58113 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de91d7bd-2974-3947-aa49-78b03dac3947 | -11.24236 | -45.19172 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1cde6dc-5d73-3e37-ba79-d9e5afdcc6c8 | -12.18764 | -57.10789 | 2026-10-02 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f3628ff-761e-37ff-8f7d-4f82dc5412d3 | -8.21566 | -55.09534 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c066735b-1c41-3f9a-8db9-c4618e251e54 | -8.41488 | -54.71166 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f9e6de6-0496-3b49-8d62-da0ba091cc8e | -11.75647 | -43.58277 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 39a5fd62-3100-3189-86e0-edd8b74bd310 | -11.78293 | -43.5598 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 580edd1c-dfff-35fe-90bf-bb80f39b5b69 | -10.53725 | -51.12255 | 2026-10-02 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6dd991a1-9bbb-3921-8bd2-7c2522426daf | -11.41216 | -43.4025 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc169d53-6009-33f9-8b14-f8ff3c99c330 | -14.33788 | -44.74101 | 2026-10-02 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67ad95fc-535e-34f5-93c2-ad092d77aa6b | -11.76276 | -43.58441 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c6ed4757-01a8-39e6-bc92-3f0aa7eef87e | -11.67487 | -43.59954 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e79b577-0136-358b-b61a-ae9ada6f3772 | -11.6658 | -43.59973 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 579ce9aa-1b91-3db7-911f-2c43ce568a4e | -13.34323 | -43.85921 | 2026-10-02 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2186ed8-0e71-3510-9e44-2e34f3f5acdb | -8.28185 | -54.73686 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee16f50-857b-3f6b-95c7-d26c282ec6c4 | -15.31528 | -42.78992 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 7aa6e482-ff7d-332d-a6cc-0b6bebcd8ee4 | -10.60073 | -50.05026 | 2026-10-02 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 633e19a5-c0fc-350d-bb4a-7f33e05b559f | -8.4154 | -54.70824 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5823a68b-1b78-3121-9503-0fc5b941a084 | -11.67215 | -43.60064 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc9fcb57-286f-3f7e-b25c-689d3931476a | -8.30649 | -54.70885 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a19f238-0834-3c19-9da5-d7831fa9b44f | -10.46136 | -47.12035 | 2026-10-02 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59319bf5-f2ed-3b65-9fc8-646f37b06b18 | -9.96341 | -54.66497 | 2026-10-02 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 199ec70b-5922-37fd-be7d-1ac9ded4ac42 | -11.64716 | -43.55789 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5634752e-25fc-3a64-86d6-3f147e81e5d7 | -8.53668 | -54.56371 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a135ccf8-9dc1-307e-bbc7-5625c77cefa9 | -15.30856 | -42.78679 | 2026-10-02 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 8904ebad-5c6b-3197-a7a8-5e708757d30a | -11.47596 | -43.42933 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce4ba570-03a4-32bf-a93f-586b63aee81c | -11.73132 | -43.44405 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b00d342-4ff0-3544-9d8b-5daa9ed8eca9 | -11.78445 | -43.56378 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc3ab306-732b-3e3a-8ea2-f767b3d1ce0d | -11.69385 | -43.60299 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0255a67e-9fef-3d4b-85a0-86b26a121324 | -8.54328 | -54.56475 | 2026-10-02 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d01eb12d-ad2a-36a1-8269-3633d4ee0f1a | -11.78141 | -43.57273 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8375c82-ecbd-327b-8e41-123e53fcaee1 | -10.25122 | -49.67325 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3edcb8a6-74c3-31ac-8d23-9818f7adbd9d | -11.24956 | -45.22741 | 2026-10-02 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 197fa04d-b208-3bc8-a901-c6f3f4fc4a0a | -9.7914 | -53.83279 | 2026-10-02 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8ad4ccd-a07d-3b0a-b2fe-69198ce2afcd | -11.73071 | -43.44944 | 2026-10-02 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55b2a3fc-b1dd-314d-9ad6-ef420d68b978 | -10.56398 | -50.07491 | 2026-10-02 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README68.md)
