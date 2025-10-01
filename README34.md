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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25d27d23-20d6-37bb-b026-fd2265d3b43d | -6.02769 | -43.78434 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72511fca-58b7-3667-8924-774758070b47 | -5.62641 | -42.8356 | 2025-10-01 04:19:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 41d6ef55-499b-3e44-95c7-09398e2ba289 | -5.24852 | -42.90096 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| adeddd41-ee56-3e5d-afc1-cfb78433e1d7 | -2.79344 | -49.62172 | 2025-10-01 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d58cb450-339b-3943-8e7e-097c20b8f31f | -9.9883 | -43.60798 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32062bf9-b6d0-31a2-80aa-20d86be7f870 | -7.4561 | -47.26525 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 742d8983-bb2d-3114-ad38-f6ccb2047adf | -6.26519 | -43.65637 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac2c57ca-39a5-38e2-8e06-c43cd8502ee7 | -5.29009 | -48.12505 | 2025-10-01 04:19:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a552ce5-b18e-3533-b8cf-d39531476423 | -6.23966 | -43.07003 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 610e1747-f694-36a0-a4e7-a97b2e904df2 | -6.23827 | -45.33244 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 58a63fd1-beaa-3958-89fd-a00f88c7b936 | -3.35347 | -43.1937 | 2025-10-01 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 410ce4e0-10a6-365c-a544-61df7e9ae60e | -6.21781 | -44.22357 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c51e97b6-baef-3ae3-9b3b-16fb2b0f8c14 | -6.35347 | -45.89621 | 2025-10-01 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97c3059d-3c69-345a-afdb-fd574433aec1 | -8.74894 | -45.92395 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc21e1dd-63b0-31e6-b5d7-e1fe270dcf17 | -7.71808 | -47.22842 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a7b454d4-3b8c-3c9e-b9b1-7141ecd4ceba | -6.46639 | -43.93837 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c66a486-3a4b-3c28-a574-7d319ca42999 | -9.93668 | -43.67265 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 763cabae-26c7-3ec3-80c6-73d674b12a27 | -5.73494 | -42.81501 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75e1eaf5-31c2-357e-9acd-b633ed6cd96e | -8.66231 | -43.98584 | 2025-10-01 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 368bc55c-bc5a-3251-87b4-6419c0637fbc | -5.84128 | -43.93407 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec56519d-fb31-3fbd-8781-8a9927585409 | -3.42394 | -46.96939 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2f80f96-9498-3500-97db-c096b8526d19 | -6.64369 | -42.03238 | 2025-10-01 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a32864c2-6d5a-3be6-b6e8-2743b5ea68a7 | -5.64989 | -43.93927 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddc4c2ff-5edd-3175-9b31-87f912d36692 | -5.9135 | -43.92756 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a11d7c05-fb77-30c4-8949-3b354ac1cb7c | -2.69282 | -54.76944 | 2025-10-01 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 243ba9e5-09a4-3f86-8904-8163d0b9f8a8 | -6.53418 | -45.22716 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e1a09ec-d867-31a7-9cad-da15546703ce | -8.61268 | -50.40111 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d346afb-0140-36bf-9a54-28de7a4b238c | -7.62911 | -45.4485 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba3e019e-b27a-3c7f-858e-d981f6cc5c16 | -6.09401 | -42.43742 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0b31558-f196-3321-a405-5e75fcb73ec1 | -6.01556 | -43.79683 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad09c19f-9fd3-3970-8096-07baa25a52dd | -3.92415 | -42.26759 | 2025-10-01 04:19:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5dbb8391-a57e-3a67-99a1-530c0288278b | -5.27767 | -43.15899 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f952e114-2c1f-34a3-a761-78d770816246 | -2.51827 | -44.1161 | 2025-10-01 04:19:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5406a1b8-e35b-31b2-803c-18808cb352b5 | -5.47439 | -43.07208 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd540b12-f591-35fe-9412-d31492985a3c | -5.94735 | -45.83921 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a108e8d-40d1-375f-93c5-dd23477b9647 | -5.63603 | -43.9194 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f46658e5-3cd9-32ae-8643-0666e11c90a5 | -3.52044 | -49.44215 | 2025-10-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f9c6786b-1bbd-3714-92e8-7989ea808e5c | -8.55893 | -44.7487 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e6c2aca-49a6-3e94-85fb-6e4bf15e6982 | -6.87871 | -44.52593 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59278a55-4b46-3d18-9091-ec3bd38123c3 | -9.89078 | -45.93699 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d928ebdc-ae47-3209-af16-773e119dc299 | -9.804 | -46.95355 | 2025-10-01 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea14b43e-5e39-3da5-a0dc-2415213aee93 | -5.93954 | -45.86696 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1abebea4-c98f-32c5-891e-e1bd8fee7501 | -6.37863 | -45.60838 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dda12c39-25c2-3e7d-a28e-63903738a3dd | -8.91272 | -46.07246 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26be720b-d69e-3adc-bcba-1b6df5497781 | -5.50638 | -42.72766 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4ceca54d-78c2-3f1e-8270-b24623ed8875 | -5.64435 | -43.93132 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f06b15a-1a2a-3958-8fcb-0ca4b29a99d5 | -6.28626 | -43.65248 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cba689e-30e7-3878-8280-7c9acda61af7 | -5.8982 | -38.48053 | 2025-10-01 04:19:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fcf0ab49-d862-3474-977c-b5140d23256b | -8.55809 | -44.6666 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b8ab0d4-f852-36e4-bec4-56813d88c5c4 | -8.89608 | -45.05103 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf431837-6010-3ffb-94df-1c7c094090b6 | -9.47489 | -45.48475 | 2025-10-01 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce18b0db-906c-3a6c-8288-aba727abfc92 | -9.47213 | -45.48075 | 2025-10-01 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4f7b9c3-f7c3-3bb2-a5b1-2678ad88e739 | -8.23568 | -45.51029 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fdd3b4c6-d4f5-3ac5-8353-507bbadbe19e | -5.2702 | -42.78152 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e0f0631-4597-3d6b-be18-33b873de7b6d | -5.85843 | -43.4048 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b4fb6dde-5d9e-3770-b098-d3bc647f516c | -6.05106 | -42.44644 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bd69c25e-aa61-3a89-912f-d82775b37c47 | -6.81907 | -44.47055 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdc06327-21c1-3c85-b5e4-6bfe2f197ba5 | -8.15174 | -44.12562 | 2025-10-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47f767d0-fe77-31a6-816d-4678cc59430c | -8.54175 | -44.68181 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 725badbf-6fd5-3a61-aaf1-61abbe47a9c3 | -3.24062 | -52.88927 | 2025-10-01 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7f35277-799f-3ea0-9e76-ebeed36d01b3 | -3.51694 | -43.23659 | 2025-10-01 04:19:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84cc891d-3cf0-350e-a2a0-bc8b2d51cadd | -4.40017 | -50.84727 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6df7cb68-1a18-361e-8881-8f0c280a75ec | -7.11662 | -46.86349 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53df959d-7121-3abc-8dff-ac6de29b9ff6 | -9.93048 | -43.69075 | 2025-10-01 04:19:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb051729-4e31-3ba8-9473-f0dc57982402 | -7.56333 | -42.41791 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f95631ac-544d-3ad5-80c6-332f8fe7a87a | -5.77299 | -43.29727 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f264434c-aa82-3ba4-9bf9-eafd0ef622b9 | -5.16046 | -43.71668 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28cbaf64-6b3b-32e6-9bdb-8e2a20df8918 | -5.64658 | -43.93876 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edc2065f-f71a-3220-ab7f-a76ced981733 | -2.55109 | -48.40768 | 2025-10-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 548cc4d8-574c-3e95-9b41-e36af50accd7 | -7.05486 | -43.29406 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e378722-09c1-3810-b6fb-7b4a0c79e937 | -6.55208 | -44.13061 | 2025-10-01 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e3f3ead-07fe-3f3e-9c3a-9d55f78d60ad | -9.92763 | -43.6865 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed4f185a-ce61-3ccf-9e3f-a77e40b6f63e | -3.87882 | -42.51917 | 2025-10-01 04:19:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b2b22812-5605-379d-a259-82506fc15d52 | -5.07137 | -42.63612 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90df7e0a-4832-3093-804d-4f9538624b09 | -5.70233 | -42.6593 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e95e5cf1-36d1-3d00-aaa1-7401362ab35e | -4.4338 | -40.74966 | 2025-10-01 04:19:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ea559a73-cf93-3ee0-9eae-1014ab3ed417 | -6.69439 | -42.8035 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 766b2e5f-208d-3703-b6d8-fbec343d44d7 | -10.21941 | -43.04002 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ee09bb6-b107-3d4a-b344-361b27b055dd | -3.94262 | -41.59501 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29dff355-acda-3e36-babb-d616a995a0b5 | -6.10432 | -43.13115 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6ab67c69-ff97-3873-ac52-212644df59b0 | -5.63835 | -43.94816 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27f88abf-e309-3cb5-a2b1-cbec08462e54 | -7.0255 | -44.45658 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6514db7a-6d6b-33b1-a7cd-dad5582dc6bb | -9.92646 | -43.67106 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6bfe091-70cb-3e27-9fa9-ea605d6c7689 | -3.21975 | -47.63172 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36b65ccd-b466-3bf3-8bff-19c08b9c69f1 | -2.51443 | -44.11901 | 2025-10-01 04:19:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80f93ee1-2e47-319a-9f97-6f9e0581cfeb | -5.70577 | -42.68645 | 2025-10-01 04:19:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 92fef073-794c-3a99-872d-4623e22f0d45 | -5.61362 | -43.90878 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ba4fb3f6-181e-3dd4-9de8-b362c0a1bed4 | -3.09378 | -47.01493 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 9f56b6dd-d43b-3a87-b9bf-e436d4f79e11 | -4.68838 | -50.47981 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 095355f4-a32e-35c1-a112-91f3ea030483 | -6.03873 | -43.60281 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81ce21af-0c82-3d13-af9a-6d185c3f6c13 | -8.9868 | -50.1968 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00f7d78a-0f39-32cf-b9ab-ae33a575910f | -9.92707 | -43.69022 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ade7262-ea87-3c08-a9ba-e49d3058223c | -8.55586 | -44.65912 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c70a99c-01ca-3ae0-8d0d-1f7cc8e55dcd | -9.95355 | -43.5834 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae43e3e9-d858-3cd2-a76a-0f05de9a1e45 | -7.79701 | -42.50718 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a8fa679e-6f08-3ea2-93e4-a8139f149098 | -6.67727 | -42.80088 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 18afd59b-fe88-3480-9470-3989f115cf50 | -5.8298 | -42.79176 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61544cb5-40f1-3e38-8af8-62b9f6dabc21 | -5.83797 | -43.93356 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bee13429-8eb4-300d-ab7f-40ffa202e342 | -7.34971 | -45.23357 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c19ece2-e08b-32f2-a5b6-4ca3dc9d0ff9 | -5.944 | -45.86042 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README35.md)
