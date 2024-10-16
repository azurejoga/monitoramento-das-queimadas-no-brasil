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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e6aa355-4051-345a-8841-74b54ea82dcb | 1.0016 | -52.2164 | 2024-10-16 00:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 096ff684-4abb-3fc4-b263-058ab2ecf1ae | -2.5259 | -47.2237 | 2024-10-16 00:55:20 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| bcc7fa92-1220-3ec8-a174-1fdc426a6c7c | -3.1098 | -54.2464 | 2024-10-16 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 507064cd-0cdd-3859-ba59-c7c8efbcabf1 | -3.1099 | -54.2263 | 2024-10-16 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 180.0 |
| fcbb2470-2586-3066-b3a4-33a8f794d78e | -3.11 | -54.2063 | 2024-10-16 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9e6eb130-d008-30f3-baeb-f6c55222738c | -3.1282 | -54.2459 | 2024-10-16 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e56c0934-915b-360b-bb4c-b0d6aec45db0 | -3.1283 | -54.2259 | 2024-10-16 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| c7e495e7-e93b-30f1-872d-516ad2d19720 | -3.2225 | -48.9306 | 2024-10-16 00:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 76def6e8-defb-3e6f-9912-e836d3dfc7e9 | -3.2226 | -48.9092 | 2024-10-16 00:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 27c35b66-5519-36df-97e6-24f68bce01b0 | -3.3918 | -44.5607 | 2024-10-16 00:55:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 4f7e8749-a858-38d0-8fcf-e8e0fb75bd8d | -3.4104 | -44.5599 | 2024-10-16 00:55:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 157.5 |
| e2c1c93d-a05f-3c4e-ba05-77f25b400dc6 | -3.4105 | -44.5371 | 2024-10-16 00:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 84b37497-c798-3e9a-b923-8a07077e9845 | -3.5107 | -43.2429 | 2024-10-16 00:55:26 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1c0547ec-31fb-3f85-a49e-40928705f0a6 | -3.5041 | -52.1659 | 2024-10-16 00:55:26 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 08725a25-c2f0-3969-9e29-cceb31deebef | -3.958 | -46.4442 | 2024-10-16 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 38272a4c-5a59-3174-a9ab-9ee925a5b4ae | -3.9581 | -46.422 | 2024-10-16 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 84d97e6e-acb7-33ac-83c7-24eb38529f66 | -5.5178 | -46.9109 | 2024-10-16 00:55:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d051e9c9-ca1d-34c1-81df-9a439ce35d59 | -5.5179 | -46.8889 | 2024-10-16 00:55:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| bad41d0c-fadf-3847-8199-77326adbc3e8 | -9.1543 | -65.3951 | 2024-10-16 00:55:58 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| ea914dc8-12d5-36e5-80d2-4c5321b232c1 | -9.4574 | -40.3641 | 2024-10-16 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 164.7 |
| df7dbbc2-028d-35bf-baa3-2888192e598c | -9.4578 | -40.3392 | 2024-10-16 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 81432e4d-0bd0-38d4-b4f6-3a9c37537c54 | -9.4765 | -40.3613 | 2024-10-16 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.4 |
| ddc5be85-5b85-3cf2-8a6b-4a83994ac27d | -9.1727 | -65.4132 | 2024-10-16 00:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| aaa2139c-3db8-33cf-9ffc-fca337f2e00c | -9.1728 | -65.3945 | 2024-10-16 00:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 90e26f81-843c-34c8-b044-9e3d5396c57e | -9.1914 | -65.3939 | 2024-10-16 00:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| efd2f961-b044-34eb-9c15-b0792b98c5e4 | -22.46421 | -44.05426 | 2024-10-16 00:56:00 | TERRA_M-M | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 19e83da9-57d2-3c7b-a35d-e853cd782e21 | -22.46266 | -44.04395 | 2024-10-16 00:56:00 | TERRA_M-M | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b54fc0b6-afa8-3247-b84b-bb76a1aa6217 | -21.48063 | -45.32849 | 2024-10-16 00:56:00 | TERRA_M-M | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 109afe7d-cabc-3e42-85ad-7608898d98d5 | -20.9925 | -55.24956 | 2024-10-16 00:56:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 8b24c667-5efd-39a3-94fc-a7b13ef9ac1f | -20.99017 | -55.24375 | 2024-10-16 00:56:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 14e5a41e-f812-33f2-ae87-902e829ba87e | -20.86179 | -49.88251 | 2024-10-16 00:56:00 | TERRA_M-M | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4bc8c3eb-1e47-3513-a773-9eab44814e35 | -20.86033 | -49.86993 | 2024-10-16 00:56:00 | TERRA_M-M | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 0522b76c-e59f-3a59-a59a-d58618755796 | -20.85202 | -49.8768 | 2024-10-16 00:56:00 | TERRA_M-M | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| b43d06d2-bbe4-360a-b5dd-a183e2ede985 | -20.85048 | -49.86414 | 2024-10-16 00:56:00 | TERRA_M-M | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| a2968b20-69e7-3a7e-8726-b4b41ce47e87 | -20.44778 | -46.55561 | 2024-10-16 00:56:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c1709c79-5df9-3fa8-a48f-cc40faf93ccc | -19.70532 | -46.7855 | 2024-10-16 00:56:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1111168c-a803-3f5e-b66d-02daf25deafe | -19.69776 | -46.79625 | 2024-10-16 00:56:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 77ff8bd7-29aa-3411-8943-d86d4113c4d7 | -19.69647 | -46.7869 | 2024-10-16 00:56:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| e1f12e38-7a07-3c6a-b040-8a8351580492 | -19.59278 | -57.00555 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 192.8 |
| ddc7f43e-31a4-3c24-8af3-47e3aa1e10c6 | -19.58952 | -56.9658 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.0 |
| b9f91a38-d813-3c5e-9aa8-af211425de11 | -19.58914 | -57.01086 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.7 |
| 92003ea6-298f-3083-b9a6-9047f7e98830 | -19.58563 | -56.97116 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 279.2 |
| 4824e38e-2311-3786-9fe1-2060e3bf9f91 | -19.58349 | -47.23875 | 2024-10-16 00:56:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 14daac1d-b54d-3639-ae52-f32ddc4c67a6 | -19.58221 | -47.22933 | 2024-10-16 00:56:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5e770422-371a-37ec-855f-1b3bb3b3f0ea | -19.57258 | -56.96739 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.5 |
| c6c42039-56f6-3b8e-a484-732fdae7b63c | -19.56869 | -56.97269 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 15ec4233-a8c2-31d6-916d-961dcc10b5c3 | -19.56559 | -44.85202 | 2024-10-16 00:56:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1320e30b-7a35-3ee6-a701-9dc9d282fac0 | -19.55564 | -56.96899 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 924e29f9-e7cf-3914-9b5f-cfe3b8d75bc6 | -19.55175 | -56.97425 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 9f6960cc-c858-3890-8173-237daa6af2ee | -18.29396 | -41.74741 | 2024-10-16 00:56:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 21b9f217-25ce-39d9-8ad8-b962a56bbf3a | -18.29141 | -41.73203 | 2024-10-16 00:56:00 | TERRA_M-M | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| cd0d0e92-671c-3969-92b4-df45fea101c6 | -18.27539 | -56.6111 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 4af47874-d9fd-3248-8909-0bb45ac20297 | -18.27206 | -56.57564 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 206.4 |
| 8a2b505c-25a1-391c-9273-bc74924eec79 | -18.26673 | -56.60679 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 161.6 |
| 5435ad7e-6b01-36dc-8f80-68e806096bb6 | -18.26367 | -56.57129 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 370.2 |
| 660501a2-e39d-3abc-aeb9-9da8b0845ab8 | -18.25914 | -56.61269 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.3 |
| ad0dfa1e-6ba0-3d36-ad6b-377daf3f16ea | -18.25586 | -56.57723 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.7 |
| c9ea9468-0212-306f-b294-f04eeebd7f07 | -18.25154 | -56.43161 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 599c7258-b040-38a2-9b19-ac610c89e288 | -17.92191 | -57.43484 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.0 |
| 7763537b-974a-37a4-b5c5-941fe6de333f | -17.91842 | -57.39429 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 0861b17a-0be2-3998-82ba-2448d71283dd | -17.90475 | -57.43649 | 2024-10-16 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 345.1 |
| 0562df9b-6b13-3a90-973e-4b38d62aa1b1 | -17.73982 | -43.91774 | 2024-10-16 00:56:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c3993cab-b50d-3ab0-a23b-80b55dad5491 | -17.73716 | -43.91258 | 2024-10-16 00:56:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ae9494a5-8ab6-3055-85ba-464222086189 | -17.55956 | -42.33464 | 2024-10-16 00:56:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d91839f3-dd15-3ac7-b8ec-c210c25087e1 | -17.55719 | -42.32007 | 2024-10-16 00:56:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 12dc247d-0b21-3e1e-97b2-5289c16ca17b | -17.55049 | -45.01514 | 2024-10-16 00:56:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 518141b9-4bab-315f-be31-98e765ef817c | -17.25736 | -42.65796 | 2024-10-16 00:56:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 26d79fbf-ab32-3981-8cde-54373dcf1f1f | -17.25467 | -42.66422 | 2024-10-16 00:56:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cdaba3f9-44f2-36da-97dd-e9ee6d4aeb8a | -17.25236 | -42.64976 | 2024-10-16 00:56:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 1d7d06a2-a1ce-3411-906a-e59d830654b6 | -17.24391 | -42.66606 | 2024-10-16 00:56:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| c523a621-242d-3bf8-a2b9-dbf4e563fb82 | -17.24161 | -42.6517 | 2024-10-16 00:56:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 868c23fe-442a-3ac0-a00b-a9a5e6227366 | -10.822 | -49.256 | 2024-10-16 00:56:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 54ef200c-5749-3158-b647-3af30b114099 | -10.8224 | -49.2343 | 2024-10-16 00:56:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 18dfb639-3b55-3c8e-966a-2b6e301272dd | -11.6915 | -65.2432 | 2024-10-16 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 52e7ffde-ca2d-3c4b-9313-b9a862eed54a | -11.6917 | -65.2243 | 2024-10-16 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2c605799-a420-34ce-b262-72546638a4f8 | -11.6918 | -65.2054 | 2024-10-16 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c311477e-7ca2-36db-a1df-4487bd4a4968 | -11.7103 | -65.2424 | 2024-10-16 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7ddeecc7-e9fc-3db2-9685-20d55c98ee93 | -11.7104 | -65.2235 | 2024-10-16 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 0490b2c8-b9a5-30c4-bd41-45f1fc3e86e2 | -12.4925 | -47.2818 | 2024-10-16 00:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9029ed26-46e2-3433-8e09-7daeb810fb66 | -12.3793 | -63.7294 | 2024-10-16 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 253297da-5e3d-3a76-8b31-8c854891c321 | -12.3795 | -63.7103 | 2024-10-16 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 88be49bd-f054-3479-8f01-e28737c5c111 | -12.3982 | -63.7284 | 2024-10-16 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d18ea26c-6e95-3393-b3ad-f34471e9dfa0 | -12.3983 | -63.7093 | 2024-10-16 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| d22f1e72-c2f8-3eab-8ca8-9052afe4817c | -12.5149 | -63.2822 | 2024-10-16 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| aab87b93-3771-3152-8416-3637df3efec1 | -12.515 | -63.263 | 2024-10-16 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 14155562-77c6-3fd0-ab06-904e5bbf2f38 | -12.5338 | -63.2812 | 2024-10-16 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 76a09f44-5a38-3999-bfe1-9e3e82ea5064 | -13.383 | -46.947 | 2024-10-16 00:56:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| d82a7bc0-01e7-3cdd-b57e-0bff3e2253f7 | -17.2439 | -42.6575 | 2024-10-16 00:56:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 123.8 |
| a66733c5-832a-3c45-b687-f8ce38d8208d | -17.2639 | -42.6527 | 2024-10-16 00:56:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 113.0 |
| f2184906-844a-3c72-bae5-6729e2f1f69e | -16.935 | -57.8538 | 2024-10-16 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 26d0e9f8-2875-399f-a045-97a82d65da71 | -16.9546 | -57.8516 | 2024-10-16 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| f7a08af3-71af-3419-af76-8b5fc650dc05 | -16.9549 | -57.8312 | 2024-10-16 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| a9fbcf84-d575-3319-910b-d4b908293e85 | -16.9745 | -57.829 | 2024-10-16 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 1cccbe2d-1299-3d4a-be79-e9d4bc085152 | -16.9154 | -57.856 | 2024-10-16 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 9e98bb06-3648-31ce-a81b-369982a9653b | -17.0066 | -58.2934 | 2024-10-16 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| d4de2c8a-c5d8-329e-a405-53ddc4fe88f2 | -17.2373 | -57.3079 | 2024-10-16 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| dc4286f3-e463-31d9-85a5-82061a4094b3 | -17.1951 | -57.4972 | 2024-10-16 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.3 |
| ef5ba56f-31af-35c6-9ac1-a732181a390f | -17.1954 | -57.4767 | 2024-10-16 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 3afd5d40-cefe-387c-b2c4-a244ff64db56 | -17.2081 | -56.6946 | 2024-10-16 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 0355a7eb-dbce-3d00-9a16-cff39cee7313 | -17.2157 | -57.4334 | 2024-10-16 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |


[Clique aqui para ver as próximas entradas](README11.md)
