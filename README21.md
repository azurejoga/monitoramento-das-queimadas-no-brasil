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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a53ecfce-ad37-39eb-bdf4-e9df4294728f | -6.97513 | -42.79234 | 2025-07-23 11:51:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 2607a9e1-8563-307f-ad31-e8907fee50c5 | -10.39836 | -46.67939 | 2025-07-23 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a65c799c-cb10-375e-8d4c-451274c4f034 | -7.04576 | -45.85545 | 2025-07-23 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 33a59c8e-0a1e-370d-96fc-78f0efee6243 | -5.62758 | -43.15534 | 2025-07-23 11:51:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 56e82db8-d073-3a4e-abd8-c3efd9652cfa | -5.79417 | -43.72089 | 2025-07-23 11:51:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e9f6d093-8d82-3a63-9840-d082d949746d | -7.26279 | -44.2861 | 2025-07-23 11:51:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 93106f88-c896-3d09-b123-2cac4a8875aa | -7.04881 | -45.84961 | 2025-07-23 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| e0e6e1d4-a4f9-30bc-bd13-d2b5ac1d0fc2 | -9.15296 | -40.15598 | 2025-07-23 11:51:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 40e82c11-da9d-3203-85da-aadb34b99cb4 | -7.70277 | -37.51997 | 2025-07-23 11:51:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 46dcd9be-5086-3f22-bb6e-d970511728f8 | -10.63062 | -45.22289 | 2025-07-23 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 259226ef-3f31-30f5-b21d-2866ac3c20f0 | -6.77431 | -39.18661 | 2025-07-23 11:51:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 9db60872-5f44-387e-bd0f-2c6c79652628 | -7.27936 | -44.3923 | 2025-07-23 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7128fb28-142c-302a-bbe3-b43d764b128a | -7.41974 | -44.59407 | 2025-07-23 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 90ea9502-6c62-3cff-9841-3b25b8d37448 | -5.62968 | -43.14167 | 2025-07-23 11:51:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 33.4 |
| b383bfd1-e23e-3cb8-83be-4a2be912e42b | -19.53841 | -41.39857 | 2025-07-23 11:53:00 | TERRA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| a5c47637-0dd4-3be1-894a-363d008d8853 | -17.98189 | -46.01815 | 2025-07-23 11:53:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 792658ae-ab53-3ed0-bd25-d1d1bbca1714 | -17.51025 | -39.94573 | 2025-07-23 11:53:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| c7d50392-8ed8-3d5e-a680-30f31e3f9b37 | -13.20929 | -44.9647 | 2025-07-23 11:53:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1e47efde-adb9-3623-b0b8-b53a789d3222 | -14.18593 | -45.34623 | 2025-07-23 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 212d9f4e-e6e1-3104-9915-9d63489ddba2 | -17.17818 | -45.8476 | 2025-07-23 11:53:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9e4c2278-d1ab-3f34-b210-b4d9d06f3d08 | -19.23387 | -40.47028 | 2025-07-23 11:53:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 1382026c-0838-3a4c-bc53-c34da9ea83e7 | -14.06552 | -42.64275 | 2025-07-23 11:53:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 9afeb072-ef95-3ae8-a7e3-ae33c51ed878 | -17.98213 | -45.99683 | 2025-07-23 11:53:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7f4f5340-7b93-356d-8aaf-4b14c7ceba87 | -17.1844 | -45.85746 | 2025-07-23 11:53:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a094a82b-5ad5-3387-a820-50202fbcbf46 | -17.18673 | -45.84318 | 2025-07-23 11:53:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 36e0ce34-b8b4-36e3-9cf2-ad211a9e8d23 | -16.30566 | -42.97154 | 2025-07-23 11:53:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e83d919b-48e4-3463-94ae-9a7af3540ac4 | -15.23215 | -45.45254 | 2025-07-23 11:53:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 39a8c877-cf92-37ab-8e21-3cea134514f2 | -18.41798 | -44.18443 | 2025-07-23 11:53:00 | TERRA_M-M | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5219db32-be62-3030-be3c-8cfa0d78ec62 | -14.74861 | -42.82256 | 2025-07-23 11:53:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| e7906cd0-27df-3da9-8f74-70bc3ce3a471 | -16.30413 | -42.98157 | 2025-07-23 11:53:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 053b9401-5a76-380d-ba91-4a1657624d54 | -19.24994 | -40.62014 | 2025-07-23 11:53:00 | TERRA_M-M | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a10e56d2-d2e0-39d9-b136-b5c9d2b92bb9 | -19.8417 | -40.60415 | 2025-07-23 11:53:00 | TERRA_M-M | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2af951d5-778c-38ec-b379-aa170df3dc28 | -16.31486 | -42.97301 | 2025-07-23 11:53:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 86666b2e-52eb-3c4b-8431-c6033ad4e7f3 | -16.31334 | -42.98297 | 2025-07-23 11:53:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c619e70e-6735-34ce-9c7f-6c2b5f17bd27 | -19.49361 | -40.3217 | 2025-07-23 11:53:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 7ee1d846-7599-382b-be11-0c203939dd74 | -17.51158 | -39.93606 | 2025-07-23 11:53:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 7a464502-b42f-3e3a-bf5f-476685b3961f | -13.56094 | -45.63832 | 2025-07-23 11:53:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 962ed90b-b83a-3b85-a6bf-56939d86ea64 | -13.70178 | -45.69086 | 2025-07-23 11:53:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 63998820-4ddf-38b5-9137-a16844eebc81 | -15.45156 | -44.49802 | 2025-07-23 11:53:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db0f9a8d-7c45-35a5-9ee0-32dcbcad540b | -20.41174 | -42.30487 | 2025-07-23 11:55:00 | TERRA_M-M | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 43e3d32f-4c3c-3f50-8c6d-6a27f9ec93b3 | -20.81277 | -42.59352 | 2025-07-23 11:55:00 | TERRA_M-M | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 045c7095-efe6-3936-ba0e-321b3e3e6ede | -20.36119 | -44.51218 | 2025-07-23 11:55:00 | TERRA_M-M | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 66a01d26-deec-3d91-b172-9186ad519e9d | -21.60997 | -41.27198 | 2025-07-23 11:55:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ba5a19a8-f5ed-3c99-ac38-2801f1871d58 | -20.72056 | -43.15417 | 2025-07-23 11:55:00 | TERRA_M-M | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| ec897733-70ad-3910-930c-d3441ad79f13 | -6.9801 | -42.809 | 2025-07-23 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 281ac729-008a-360c-ae75-378e08b1f959 | -6.9804 | -42.7854 | 2025-07-23 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 206.5 |
| 5d10f0eb-4534-3cdf-89b1-a305fb80bce2 | -5.9213 | -43.4636 | 2025-07-23 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 6ca5b086-508a-31dd-881b-b45f5f7f530b | -7.2822 | -44.3876 | 2025-07-23 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 756827d1-951d-3ccc-a9c3-975e5f8c5aeb | -6.9801 | -42.809 | 2025-07-23 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 89828fe5-5954-3d8a-b330-5749f694340b | -6.9804 | -42.7854 | 2025-07-23 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 189.1 |
| e2ea9c67-982f-39e0-b92b-3e1e0253d5a8 | -10.6363 | -45.2257 | 2025-07-23 12:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 779f3d50-10ff-33f6-9be7-7a8ca9a5336b | -7.2822 | -44.3876 | 2025-07-23 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a9a0cbcc-5f01-3850-87ce-75d14d0402ba | -5.9213 | -43.4636 | 2025-07-23 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| a80086c3-335f-3771-ad53-a6724501d7e0 | -6.9801 | -42.809 | 2025-07-23 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| fe785b87-ae71-3356-a2f1-4fdf4f687444 | -6.9804 | -42.7854 | 2025-07-23 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 149.5 |
| c179684c-7ca8-3496-a271-61e780ef9e46 | -10.6363 | -45.2257 | 2025-07-23 12:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| ba0f8c0b-c470-3168-9455-a90406bb0524 | -5.9213 | -43.4636 | 2025-07-23 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| dc342253-635e-36ba-b6ab-06e2e7b6d4f3 | -6.9804 | -42.7854 | 2025-07-23 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.1 |
| f87ad58c-72f9-3daa-9881-d89d8f0f9d00 | -10.6363 | -45.2257 | 2025-07-23 12:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 07c6dec7-f703-3902-85b1-40fb60007347 | -6.9801 | -42.809 | 2025-07-23 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| e5602610-d5e6-3173-8092-3d6a59c91ea2 | -7.2822 | -44.3876 | 2025-07-23 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 229.3 |
| ce7d16ac-5116-3bcd-ac1f-890848e0692b | -4.0569 | -42.5118 | 2025-07-23 12:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 09ebc066-605b-3c5f-b4ff-244a5cc370d0 | -6.9804 | -42.7854 | 2025-07-23 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 9b4457be-bbb0-3157-85f6-eda59f97178b | -7.2822 | -44.3876 | 2025-07-23 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ecf14e2e-4305-363f-bf76-4f8fc6a99fad | -5.9213 | -43.4636 | 2025-07-23 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 7c3802c1-98ab-3e6f-b1d8-6b5c54d0f048 | -10.6363 | -45.2257 | 2025-07-23 12:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 7970d180-7b65-30de-85c0-6a20f4417c78 | -7.0224 | -45.8428 | 2025-07-23 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 19943c08-01a3-380d-9bb3-ad7f6e545183 | -12.3628 | -63.4245 | 2025-07-23 12:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d4d09c76-c3fd-3d13-89cd-5ea2672b68d6 | -6.7452 | -45.4604 | 2025-07-23 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| faa511a8-30c7-3c8f-a166-b89ed28e6a27 | -7.2402 | -44.7812 | 2025-07-23 12:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6a2a2a37-8f85-326a-b8cc-d5fcc75e0ea9 | -6.9801 | -42.809 | 2025-07-23 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| b139e4cb-8b3a-3477-a433-8a03c8d0172f | -4.0382 | -42.5129 | 2025-07-23 12:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 28aad0b9-ce0b-3e27-be4d-d76f6d90cc2a | -6.9804 | -42.7854 | 2025-07-23 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 186.5 |
| 3c68e77c-fe57-3fa3-a82d-acf809e5ae77 | -5.9213 | -43.4636 | 2025-07-23 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 6ee4ccc1-a44a-3c28-a7b9-eaeef3f8dfc4 | -12.3439 | -63.4255 | 2025-07-23 12:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 945badcd-329e-3df1-9998-35057539f298 | -6.9801 | -42.809 | 2025-07-23 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 948d4213-5cb2-3fd1-ac29-453ee7632624 | -12.3628 | -63.4245 | 2025-07-23 12:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 9eba3624-82a3-39d8-854d-6a1c3d60989c | -7.0224 | -45.8428 | 2025-07-23 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 33058087-08c3-36e5-9bbb-d83f5734e9a5 | -10.6363 | -45.2257 | 2025-07-23 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3cef3e8d-255a-316d-832e-f531d2b66e61 | -4.0569 | -42.5118 | 2025-07-23 12:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 7a720766-1e0b-3530-8960-cb043727f99f | -7.2402 | -44.7812 | 2025-07-23 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7c7ee02b-5596-3a5e-abfb-dff4a1b33124 | -7.2822 | -44.3876 | 2025-07-23 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| def52c74-9952-35ee-8357-d45001da8c75 | -7.4113 | -44.6051 | 2025-07-23 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 8ea46539-abd7-392e-9758-6179ccf7a44b | -4.0569 | -42.5118 | 2025-07-23 13:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 131.0 |
| 1f07f6b5-c43f-37ec-90e2-1efd2069e92d | -7.0224 | -45.8428 | 2025-07-23 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| d13ae0c9-3a99-3587-ae97-c3d4f10b42c2 | -6.9804 | -42.7854 | 2025-07-23 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 231.5 |
| 5734144f-f352-3833-8d8d-4e07f1e8f2e8 | -10.6363 | -45.2257 | 2025-07-23 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9ab41bff-afa9-3897-80e8-9d5bc0a80024 | -7.2402 | -44.7812 | 2025-07-23 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 06c3fbe0-4016-33ff-aa35-a86664932351 | -5.9213 | -43.4636 | 2025-07-23 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 85e23b72-dc18-3e02-ae7f-0282bd3d903d | -12.3628 | -63.4245 | 2025-07-23 13:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 412c65ba-864b-33d8-bc1f-9f5ea12aad28 | -7.4113 | -44.6051 | 2025-07-23 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3ca76ae9-666c-3852-b6d2-8dfb79076bf4 | -6.9801 | -42.809 | 2025-07-23 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 6587735f-f63b-302b-9752-ba59873fea03 | -10.5264 | -46.1731 | 2025-07-23 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a4aa80ec-302f-3106-bc38-624fac0187c3 | -5.9213 | -43.4636 | 2025-07-23 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 174.9 |
| ff156959-4e45-382d-8d5d-055cca5b6c80 | -7.2402 | -44.7812 | 2025-07-23 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 6a10804b-be7e-3a45-94ad-08895fc397e5 | -12.3628 | -63.4245 | 2025-07-23 13:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 8dc8d3ea-ad98-3a07-9321-af165b38199b | -6.9801 | -42.809 | 2025-07-23 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| bf541b4f-3778-3476-a61e-21aacdab3a57 | -4.0569 | -42.5118 | 2025-07-23 13:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| db6b84d3-bd0d-3fb7-a72e-398433d66212 | -4.0382 | -42.5129 | 2025-07-23 13:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 627df56f-3e90-3c56-bd2a-c128a2cd29c7 | -6.9804 | -42.7854 | 2025-07-23 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 150.8 |


[Clique aqui para ver as próximas entradas](README22.md)
