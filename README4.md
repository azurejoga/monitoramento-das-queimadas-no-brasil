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
| 9674e8bc-ea80-3220-a684-9dedad4152da | -12.7529 | -44.424702 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97bda346-23d2-31bd-911f-8022cacbda9e | -5.2295 | -43.195801 | 2025-08-15 00:21:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87eb819c-ec09-38fa-9855-28f40dd73278 | -8.296 | -44.998699 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84136c64-173c-33de-9ca1-cf8ce37b6c05 | -3.9572 | -41.484798 | 2025-08-15 00:21:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44d4e65f-6d1c-3a97-a429-777deaeb3c3c | -22.606501 | -42.100498 | 2025-08-15 00:21:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1811edb4-8ac2-334e-8afa-f38361b5bb8e | -8.5999 | -45.628601 | 2025-08-15 00:21:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea37bce-c13a-3b19-9fdb-c4d9ccf68b28 | -14.7975 | -42.722801 | 2025-08-15 00:21:00 | METOP-C | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 830e6a85-c721-3612-919b-e4cbac6a3573 | -12.3151 | -44.347198 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0600dea-379f-32ef-bcaf-7f3c465cb232 | -3.4352 | -49.0485 | 2025-08-15 00:21:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fde78cb-82c1-33e3-861a-d8e97631d12f | -8.1917 | -42.257801 | 2025-08-15 00:21:00 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc4ae752-a1fd-3fc6-bd0c-b15083b2716e | -7.3924 | -44.869301 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 927ff78c-25f4-3a6b-9974-97eda02c46b5 | -6.9715 | -42.874802 | 2025-08-15 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9678630e-1850-325b-9970-9647699e10e1 | -20.9769 | -47.409 | 2025-08-15 00:21:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 33fba8ca-1b1e-3826-b110-3d9582d2a2c4 | -8.5981 | -45.620499 | 2025-08-15 00:21:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de230972-dda2-36d8-ba7c-6217551767ae | -13.3168 | -45.240299 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f7ffa636-22b4-3b09-b536-a34549d5b41a | -4.9817 | -41.719601 | 2025-08-15 00:21:00 | METOP-C | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f61b1ec-b812-3779-aa58-2ced428d1632 | -6.22 | -43.332199 | 2025-08-15 00:21:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e27c3184-2510-3b8b-bfeb-d2f0debc37f3 | -22.604799 | -42.092201 | 2025-08-15 00:21:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d2aab3c-173c-3e6d-96c8-8b5fcd2ab44f | -5.6118 | -43.4688 | 2025-08-15 00:21:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd110cad-daf9-3094-808f-521f17ac57fe | -7.3778 | -44.895802 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35a2f89e-b071-3110-af22-bcdb05572067 | -5.685 | -43.6535 | 2025-08-15 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a7aee97-ed1d-381f-8fff-771461619fe5 | -6.2232 | -43.345798 | 2025-08-15 00:21:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b86465e-5a0b-3405-9648-7380ad34f1de | -12.5809 | -46.9515 | 2025-08-15 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3320331-b026-3d16-8939-45d45d6863bd | -2.5374 | -47.7108 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294828c4-e7e9-353a-8a5b-95446ab1a8bb | -4.597 | -43.316399 | 2025-08-15 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50dc19cc-afa1-3173-91bb-ba1c23b4b6c9 | -2.4845 | -47.5686 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 702940ce-955e-3b28-ac90-563fa1d23cbd | -7.5689 | -47.056801 | 2025-08-15 00:21:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b596857-13e1-36c9-b2b4-a165b48767a3 | -2.9087 | -48.3064 | 2025-08-15 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b7f97c-510e-3c08-b995-9c85b591afdc | -7.8534 | -48.2229 | 2025-08-15 00:21:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 211e1e81-5168-3f52-9289-621b08544355 | -3.8189 | -41.555801 | 2025-08-15 00:21:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| feecfd94-ba87-3122-9935-72e9456b9e27 | -8.3108 | -45.019299 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a34814d9-4e23-36d2-8b91-ae31d31db8a5 | -5.7589 | -46.672401 | 2025-08-15 00:21:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae9d1001-ce18-365f-ab38-197a0b663824 | -8.5234 | -43.305199 | 2025-08-15 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa8af4de-0c79-3746-b0a1-749bfbd9da20 | -6.3359 | -42.8022 | 2025-08-15 00:21:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d307e0e0-4ce7-357c-b408-0394c7e447bd | -12.3053 | -44.3493 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9ac9559-ba0a-31fe-bd12-fd9855c34735 | -6.9514 | -44.555901 | 2025-08-15 00:21:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b35da47-57c0-3892-9525-48d4fe5068c5 | -8.3125 | -45.026901 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dafc0def-b816-3ebe-9aa7-c25f4ec5b8b9 | -7.3989 | -44.852501 | 2025-08-15 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37f6e4ca-41a3-3ab1-86fc-9fe71aee7581 | -5.5391 | -45.3717 | 2025-08-15 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd0a8a50-62a7-34b9-b4f4-94c9084af4eb | -21.2848 | -44.036098 | 2025-08-15 00:21:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40d7a0fa-4ea7-3bc2-887e-4103184a44fd | -7.3941 | -44.876701 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e692501-628d-3716-94bf-e4e585d0717c | -9.2678 | -50.2314 | 2025-08-15 00:21:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa5869db-41e2-3cb2-a587-6d344ee0f151 | -15.4054 | -46.604401 | 2025-08-15 00:21:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 375c8bb8-e715-3f39-a869-2038941d209a | -2.4826 | -47.560001 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9f1ff42-c0b5-3395-b3b5-2d1288349a96 | -13.4711 | -43.7584 | 2025-08-15 00:21:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 607d7534-c78b-331d-a9de-daa621c700c0 | -14.2439 | -44.587299 | 2025-08-15 00:21:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1e9c77-1355-3555-af86-98be7be4c07e | -21.190599 | -45.682201 | 2025-08-15 00:21:00 | METOP-C | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4f1960dd-4ee3-3da6-8f53-510ef7e30adb | -12.7609 | -44.4146 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23266325-5e89-336c-98e6-4211c1097e34 | -13.3266 | -45.238201 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 038cd489-4d60-3709-a94b-643d9169a2f2 | -13.3229 | -45.220501 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 705dcb76-d10b-3c5b-bae2-eff3f6e326ba | -7.3859 | -44.886299 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13de95a6-a4e9-363a-bfb4-65ccd641f69f | -5.2264 | -43.182098 | 2025-08-15 00:21:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83286591-7f90-3907-bc96-e9eb21098718 | -4.1859 | -42.427399 | 2025-08-15 00:21:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd05b2d3-b808-307a-a92f-39bceabb8603 | -12.6821 | -44.9543 | 2025-08-15 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8017495a-6bc0-34d0-b1d0-771b6a7726fb | -6.5884 | -44.636501 | 2025-08-15 00:21:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cf298ba-cee0-30eb-a3be-f6aef8b83403 | -9.1919 | -45.330799 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd52d89b-29e5-3bdc-93a0-2de0ad8ea74c | -22.614599 | -42.09 | 2025-08-15 00:21:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72277148-4ec7-3957-ac58-91930dbda1d6 | -3.9554 | -41.4772 | 2025-08-15 00:21:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 977b2adc-6034-3a66-b0f1-dbf5a60f6b95 | -17.501499 | -47.8368 | 2025-08-15 00:21:00 | METOP-C | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e46a27a-9f29-3511-b3b4-3bc802ff365a | -13.3131 | -45.222599 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 223389c4-9796-396f-ae6a-9f22c3b29b09 | -13.3149 | -45.2314 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0654493-e793-3f20-82ca-2c566d1f4f5f | -9.048 | -40.517502 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1aceb721-01b8-36b9-af9c-e64610ff0e3c | -11.3657 | -55.4107 | 2025-08-15 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 2a666b16-30cd-3511-aa0e-2fc9f4466ec6 | -9.3875 | -60.5528 | 2025-08-15 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 03f9c3f9-e296-3417-90e7-6ad37b1fe47c | -7.0797 | -59.2157 | 2025-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 374be1cd-8910-3455-b84f-fa9c2c8e3c67 | -5.455 | -60.1391 | 2025-08-15 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 81cb8afe-3573-3877-ac38-e32dece9d9e1 | -7.2931 | -60.6287 | 2025-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 072a574c-3884-35d3-8382-7f76ae807bb7 | -7.5291 | -61.3444 | 2025-08-15 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2749589a-25b8-3f6a-a5af-e4211cb34de0 | -8.6038 | -45.6256 | 2025-08-15 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| d96ddeb4-5522-3c3f-8f31-808ae5e6207f | -6.49 | -62.9306 | 2025-08-15 00:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4a3b3656-f314-3238-8706-f6df8b74d2cf | -14.2444 | -44.5897 | 2025-08-15 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1e41d4ef-5832-31aa-9113-5ef61b10aa2d | -9.4992 | -60.547 | 2025-08-15 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 263b8c40-0aff-3936-97e6-0776623c6791 | -2.4876 | -47.5737 | 2025-08-15 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 02743706-9772-3343-8878-6c672f3abc23 | -7.0613 | -59.2165 | 2025-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2561a4c6-384a-38f3-b42b-6dcd606ed0e4 | -6.9302 | -59.5497 | 2025-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0ac619a4-569f-3c84-bfb3-f4646bb3f33a | -7.5292 | -61.3254 | 2025-08-15 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| c1a3eef8-561d-3c8a-8548-04a512feaf80 | -7.6104 | -63.4972 | 2025-08-15 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d6eadbc8-3a10-38db-8890-145bd7974616 | -7.0796 | -59.2351 | 2025-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8196b1cb-426c-388f-b1d2-1d21f99df6c5 | -8.3099 | -45.0196 | 2025-08-15 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ad874737-4e50-3af6-a2d6-89bd37eeefc5 | -9.4994 | -60.5278 | 2025-08-15 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 8556d1f3-e9df-3304-b7ca-d5bc10576782 | -5.455 | -60.12 | 2025-08-15 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 207c4867-09a7-3c1f-9122-d151171c4310 | -11.3468 | -55.4124 | 2025-08-15 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 206.7 |
| 09966469-cc3a-3102-9387-c379819ea5a1 | -9.518 | -60.5268 | 2025-08-15 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c7aca0a9-3e65-3ac0-9ae3-e707c317bf09 | -11.3655 | -55.431 | 2025-08-15 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 18d7330a-eff6-3d2d-b915-f22ea7cd8e5c | -9.0357 | -40.5219 | 2025-08-15 00:30:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 205cac46-2079-356b-b336-77ee924832f2 | -5.4366 | -60.1397 | 2025-08-15 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 6c1d7882-c6a9-3ba9-99e3-451e437dbb5b | -6.9303 | -59.5305 | 2025-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 22316ca3-1fc2-38db-a179-39885bb4e425 | -3.4254 | -49.0517 | 2025-08-15 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 52455d46-ae8d-3308-af8e-3afa98e2910a | -9.4995 | -60.5085 | 2025-08-15 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 867cdfe6-9543-33c7-b7b4-7cea7b74c471 | -11.3466 | -55.4326 | 2025-08-15 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 64de84de-826e-3a7f-b871-144b461abf6d | -7.6103 | -63.516 | 2025-08-15 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 40b862d8-b871-30b2-81eb-e0bca9be0d0e | -5.762 | -46.6741 | 2025-08-15 00:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 33d7fa39-11d4-34d3-92e7-cd9409fe355a | -7.3116 | -60.628 | 2025-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 76e34343-997f-34ee-b65c-d67e7293279a | -8.1029 | -61.1878 | 2025-08-15 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6b03cda2-e386-37c3-bad9-d49568cd7558 | -2.4876 | -47.5737 | 2025-08-15 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 5748c909-f998-3ead-a0f7-0b42f4c316f1 | -8.3099 | -45.0196 | 2025-08-15 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3417d30f-c08e-3ad0-8103-78ab724307d6 | -7.0797 | -59.2157 | 2025-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 8293d930-1968-3d64-8b3c-8f14a7483d0b | -11.328 | -55.414 | 2025-08-15 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 5fe0ba9f-a682-3a7f-a6a4-9af5fb053168 | -9.0357 | -40.5219 | 2025-08-15 00:40:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 24542cfa-c773-3da1-9174-a26c0e16b080 | -9.4992 | -60.547 | 2025-08-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |


[Clique aqui para ver as próximas entradas](README5.md)
