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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71755b24-4ea4-363c-99cd-b416a5f31b5e | -10.26786 | -44.0262 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9dd5a213-be52-3448-b260-db5cb97132ad | -7.30551 | -42.30989 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d7f75227-b8b5-394e-a7e0-3b9c15a16c34 | -8.23381 | -43.44088 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89f07d86-ab34-39f1-80aa-330a759d26e3 | -9.62456 | -49.12844 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78f44738-c51f-3529-8b08-a1720d4d9a25 | -5.91174 | -44.7461 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c05edacb-57ec-31c7-acde-61f50f89941a | -5.74553 | -49.01848 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1de900c-2b2b-3f2a-a85a-5c0c504213ff | -8.19984 | -46.93248 | 2025-10-17 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df2de4e4-2335-37ab-a3ac-e2069bb0f075 | -6.54767 | -43.91961 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6bb51e77-911e-3429-8d7d-ec495a7a8e17 | -6.29348 | -45.49871 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f8b6ca4-1b00-379a-85a2-bf808a5e9010 | -6.40905 | -41.89414 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8de3b52-b225-30d5-9865-a3fade256f06 | -6.22006 | -44.14514 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 553fa3dc-508a-33c3-8cc0-9d9ace206388 | -6.31127 | -44.71779 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e07011fd-8339-3771-a97a-4853187c2df3 | -7.02819 | -41.82255 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7ddc556-eb18-32d7-92cc-87e82c9ebd8a | -6.36108 | -41.48507 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6e0e9de0-367f-32c2-8cca-1ae4a44090f4 | -6.78098 | -44.65081 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69844507-1aaf-3bbe-ad60-777aa2161bd4 | -7.48284 | -42.75504 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 952b2567-812b-3102-9471-fa084f01e9c2 | -7.14584 | -46.71154 | 2025-10-17 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78db9fd7-d9b7-36b8-99a3-630e5cb159d9 | -5.96729 | -42.87325 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7b7cefc1-58b3-3e58-be10-a97dfe1a392a | -6.13948 | -44.28825 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 866d3769-2b36-30c6-b01c-09a41994ddca | -5.60504 | -42.69218 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f8aa1be-7470-359d-b51b-10bcf55fb5a5 | -10.42842 | -45.02018 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e8657a1-70c1-3ae3-9929-5e44c97c7e3c | -6.95036 | -47.72297 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c32bc01d-08da-3896-9427-7531f8c51f9c | -3.50473 | -52.48813 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 73415241-aef5-3bb0-a453-63b686ad4079 | -9.14398 | -46.65023 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| edd77f7d-211e-3227-bb0b-4b2bf6b9869a | -5.37214 | -42.72374 | 2025-10-17 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b9019f66-35c1-3f5b-ba10-4edd93ffd291 | -7.46072 | -42.14935 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 34ca81cb-9b12-3192-9553-944bbae8c8ee | -10.72596 | -47.58957 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc8b148c-486b-3f70-9977-1c2221d9451c | -4.01498 | -44.18894 | 2025-10-17 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fe8c4bc-70b9-34cd-be68-9206a089f178 | -8.08171 | -46.66499 | 2025-10-17 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c3ac136-21ea-3287-95d5-b2596b289f8e | -7.00157 | -39.89489 | 2025-10-17 04:19:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b2e7e17-52a5-38d8-a90f-5844b64e82eb | -6.2414 | -41.54485 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62bffa2a-12e4-36f5-9e58-0f52ef8d7a92 | -10.10568 | -44.57677 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a64bd82-1fe2-3ea6-a7b7-4ead66d290b9 | -11.39421 | -44.21268 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feb188bb-5027-34f9-a12a-485ef2c8f338 | -5.09563 | -45.43097 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed95cf5b-1b51-354e-a28e-b7e9ca4f59dd | -8.30019 | -43.40191 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0039a250-bc34-323e-90bc-617b23bd2fbf | -8.29791 | -43.3941 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bacd578e-14d2-336e-9db3-3b11d641f5c1 | -8.44543 | -48.74869 | 2025-10-17 04:19:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 473a9f3b-58ca-3d3f-a08c-cea73a17854c | -3.87346 | -51.94812 | 2025-10-17 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ee00362-9d60-30b4-885c-c472157eb77e | -7.13365 | -43.78101 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d69c576-d1ff-3979-8d64-b91814ce13f8 | -8.6083 | -40.19617 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e079eeac-c0a2-3219-94d1-54680609189f | -10.28806 | -44.02934 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5b66fbd7-b9ef-3744-bc8b-cca9a6a34f29 | -4.07958 | -43.40229 | 2025-10-17 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc74c4e0-a8e2-38b8-8daf-b0e07b85a1a5 | -8.09035 | -45.43651 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29923d3b-89d3-3773-8aad-cf952be4d020 | -6.09431 | -40.88756 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1fac8a8e-e8d8-35be-b74c-83e6e29144e1 | -8.15734 | -47.98207 | 2025-10-17 04:19:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 507733b3-2e9c-3110-b328-8ac7a88ca294 | -6.68661 | -44.29333 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f1e9329-ed70-3032-8946-bb5b253376d7 | -9.1479 | -46.64718 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5959e3bd-8ae9-3097-aa8e-4c2fafe8e97f | -10.50781 | -43.38911 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a961fd4-8f50-3154-93ce-856563d6c6fb | -8.2917 | -43.38939 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e6b435b-973b-3529-8870-eb5d8bb358af | -8.12457 | -45.54161 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06c589b4-46f9-35d2-a286-2ceb418cefba | -11.46457 | -44.2499 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aee20d56-6fd2-3447-9439-23871bfb27b9 | -11.47696 | -44.28182 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 003550c5-783f-3405-9e25-c35b55a21a30 | -5.89216 | -44.82771 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31c623d0-25c3-3589-a616-78097ac39b7b | -5.1567 | -44.56958 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f47c1cf2-1372-3015-8fe7-6de6011a6422 | -7.9502 | -44.11016 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ad5be21c-9cfb-3065-a0bf-c58d9008e4ea | -5.26854 | -43.26124 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ec92bb2-f95e-3960-b730-0a21cebd2a87 | -5.35377 | -43.14743 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59e7b3d1-8ac7-3df4-b185-cd44f625f383 | -9.03159 | -47.71982 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca43bf25-b4ac-36f2-895a-675ac601aaf8 | -4.55229 | -50.60551 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1b02856-683a-39a8-97ed-f298f3367614 | -4.49701 | -49.6402 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bf4e9b6-e962-3c6f-ac6c-f3ebc6c48362 | -8.4571 | -44.17461 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 73104298-a029-3bde-88e0-728bf9e37216 | -4.86955 | -45.78402 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed631430-85b7-356a-bbce-35ed4df11676 | -10.50666 | -43.39676 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1e2eb18-5569-39f2-ada8-76e7befcbb3a | -6.31501 | -40.93938 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 910a57ee-bff0-3b12-b4c0-38af9e5abf96 | -3.35448 | -49.94041 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75e7856d-0921-3b1c-a907-328a1f169d0c | -11.4682 | -44.04286 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d049528-6872-377d-8840-dc1bcd709f6d | -6.49338 | -47.49647 | 2025-10-17 04:19:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bea6465c-cebf-3957-861d-e625c279fab5 | -4.71665 | -49.62524 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5fb2e2a-3eed-3c33-868a-668b9b3ad349 | -8.231 | -43.43671 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cec7c0a9-e2d3-3d9d-a81e-db12c0e12b13 | -9.15358 | -46.626 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fd016da-5b94-3d0f-a126-374fdcea8dd1 | -10.58968 | -47.3914 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31cd75f8-71fa-30f1-80ab-c5eacd62a5cd | -5.88391 | -43.90101 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfad5af9-664f-3aed-b02a-43c0d143d351 | -6.69486 | -40.86885 | 2025-10-17 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8bbcf020-fb22-3ee4-9e6c-dbfa607cd722 | -5.33513 | -42.55687 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e55626ce-a4f0-3058-9e42-1cae8bf9899e | -10.51708 | -45.12803 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b77a91a6-cfb7-3fd7-bee4-19c6ebdaca1b | -8.30528 | -43.41392 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9dc7e1a3-3c0b-3d25-8395-16de7a03c213 | -8.21676 | -45.04571 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d644553-babe-38a2-a379-ac72b67e1c9f | -8.24997 | -44.01944 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12d7b42d-b356-3fe3-9814-14ce5fe73315 | -10.01565 | -45.50794 | 2025-10-17 04:19:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82923381-2618-3618-9e09-3532c0c6831a | -6.29292 | -45.5022 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c52bfc61-8a49-309d-880b-e3c503116511 | -8.21266 | -43.9738 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04dbd261-3d31-34ef-9750-fd975a7239d8 | -7.56486 | -41.00818 | 2025-10-17 04:19:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42552daf-7ac7-3ee2-8a63-8178ef6460ac | -7.24306 | -40.7469 | 2025-10-17 04:19:00 | NOAA-21 | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8046e7cc-c4f8-3a25-ab36-0f255265a7c3 | -9.02321 | -46.61621 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2eab5fa0-652d-3120-a6e7-c83af0b9eba1 | -7.46771 | -43.93044 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c560872-75a8-3411-ad45-5fa9a64ae2f4 | -6.07268 | -41.91164 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f93791e8-08c1-30c0-a2f2-7d244b83d2af | -6.29181 | -42.97496 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67cdb782-0902-389d-9d4e-d9491df3f115 | -8.2789 | -47.11789 | 2025-10-17 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f00c3213-c67f-3d28-bf57-3361258ce9a7 | -6.43547 | -43.91983 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dc55482-c077-3be1-bbdf-c6d32fd47771 | -10.47209 | -49.18829 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e3a36482-3e58-3920-a5a1-c869799c2841 | -6.54381 | -43.92259 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ddf3af9-0cb2-32c1-b7f3-0ca7d014b5c9 | -7.08559 | -44.26728 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23dc91a4-0209-325a-ad44-bb7d69b3d003 | -11.40654 | -44.19957 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ddf45d4-eb88-3acd-ae81-8a5cb111a11b | -6.39827 | -41.48252 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 46ed1704-02a0-3282-a991-551e6ba88d21 | -10.50672 | -43.4197 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e8cbaab-6264-3909-a88d-368d22988d9f | -11.27828 | -44.02161 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc6ea93d-2b4b-36a1-9a91-34925042ca1a | -6.53584 | -55.05003 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c640c3-a1b1-3f78-a85f-b26509dc7f16 | -7.44644 | -46.65725 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea23cbd2-9b4d-3b28-b6b3-503fcb41ca00 | -11.14016 | -45.84676 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2afa669a-cbcc-3693-87ef-9df1245acea7 | -10.17477 | -44.78962 | 2025-10-17 04:19:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README53.md)
