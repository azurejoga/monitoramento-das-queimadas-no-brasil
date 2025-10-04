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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d1e02d6-589f-3b24-9244-58dc064f996e | -5.95516 | -43.48945 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6a74ad1-42be-3a0b-bb6f-84dda9a50936 | -9.34792 | -45.79361 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eec37cef-223c-3c85-94bb-268370214acb | -9.89932 | -43.73471 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 73ccf4fd-adf7-3bf7-9607-6132ce68778e | -5.69262 | -49.30965 | 2025-10-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98dbf792-5510-3bb2-aac0-9c77cd234087 | -6.37113 | -43.8947 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e4a59930-b874-3587-8d06-d453d25c952d | -9.32761 | -45.76509 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b227656-8bbf-3391-b387-0e6d3fb5317f | -9.94925 | -50.24557 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a90ad611-c616-36e9-ac17-a868c346b618 | -7.80457 | -42.53958 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 106513ac-65e7-3710-a2f1-0139fe9f93d2 | -8.97733 | -46.72839 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0ca3433c-2074-393f-ad34-0d3a8ab0b35c | -8.62673 | -54.97227 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a47ee0cc-3cd2-3d2d-bc69-9f2fe518f0e5 | -2.89927 | -50.72602 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 921e92db-4627-3070-b17e-970571f0f4e7 | -5.77772 | -42.9229 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 6f29518b-5c85-3978-8d6a-562679c73c7c | -4.44386 | -43.23904 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 8722f36b-4d52-3412-bd79-2877e4eb9cba | -3.30479 | -48.70939 | 2025-10-04 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10fae818-dbe5-3c0f-aa84-92f2b7393029 | -9.34781 | -45.78242 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 746c7428-997b-33e8-9936-d0ba74193523 | -3.86394 | -51.81301 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| add432d0-bdde-3344-995b-d6281041df01 | -9.3426 | -45.78837 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6180e8f3-bfcf-3790-98d1-542d8516d696 | -3.84251 | -41.56159 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 83581363-bbaa-3202-ae40-c32f9a77939e | -4.61523 | -43.14967 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c913c6e1-17c1-3261-8786-16e6b3fca019 | -8.8933 | -47.60005 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 604677ec-3a49-3ac1-b025-6686142fdae4 | -6.09437 | -43.48864 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57d684a3-1c15-37d7-a9f4-350090a55efa | -9.66634 | -48.22791 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 626c2d54-f5ba-3e3e-b678-002f7fbdd1f9 | -6.66289 | -42.83173 | 2025-10-04 05:04:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| af27c99f-5a00-33cb-87bc-6f52942f0386 | -8.51756 | -50.03586 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad94743c-2cb9-3d62-8634-990292985962 | -8.1779 | -44.13033 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bbbc3d1-b91a-3d95-bfb7-fca4e6661c28 | -6.43208 | -44.45881 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3a37b49-a316-38b7-b7c3-2f6920d5ab47 | -8.91014 | -49.70468 | 2025-10-04 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b7ddc9f-365f-33b8-8c06-2473df3d1da8 | -8.61666 | -54.97075 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09db9f9e-c1f6-3008-ae9e-73c8ae74e307 | -2.69647 | -52.81761 | 2025-10-04 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 337df8fc-8612-3ffe-ab7b-cb2ab8815bb2 | -8.0628 | -44.80385 | 2025-10-04 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d01c17-9a87-317a-b0c3-26faf7946045 | -4.61447 | -43.15515 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| aee07b33-8d44-32e7-bdcb-8b9bd34130cb | -8.22131 | -55.20197 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7e26709-3af4-3929-a07b-d793a1097467 | -8.90961 | -46.60163 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f4a7ed9-6fcc-3a09-a8a6-01420ba4b166 | -4.25709 | -48.56361 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ee10143-c4ea-3efe-b862-572b36508efd | -8.05407 | -61.27473 | 2025-10-04 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc1216a8-fbe2-3b46-82ab-b720dfb1a21a | -5.63499 | -51.36797 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4df9d6f-58fc-37cf-84f9-409d33fbd5aa | -6.18111 | -43.91985 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 021c0092-7abc-3886-b320-a60ac4474081 | -8.64487 | -54.59248 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 341f33d2-e621-3f3d-9423-318a7cdb1be7 | -6.24805 | -45.35468 | 2025-10-04 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 20c9ce97-4ac1-3f2f-bdce-e7adcedfb50a | -5.08616 | -44.09424 | 2025-10-04 05:04:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ca0ba2a-1177-3d34-beb8-305c03ad1e05 | -3.2459 | -52.4094 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a20babd8-3d1c-3245-af37-8b39b9177d09 | -7.0497 | -42.78098 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3c48ed0c-55a5-319c-9724-7a453d88a3be | -6.27662 | -44.04422 | 2025-10-04 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28b91902-c127-3361-b199-4bf4647d2732 | -4.60947 | -43.14648 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cded12e6-1773-391f-9171-430f6bbefba9 | -3.19845 | -51.68164 | 2025-10-04 05:04:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 661d77d6-a0ec-3e92-bb67-fb0f915fbc9d | -6.65168 | -42.81057 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b419c9e8-c127-3f1d-86b6-5d34efd257db | -9.33349 | -45.76606 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9886951f-b7f1-3676-8bc3-49e187ab7950 | -7.71739 | -42.56344 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| beb3843d-4f83-3bee-aa74-a5d9386fbc71 | -7.74458 | -46.30983 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e182220-2ee6-3d48-a884-a1f3624e53c6 | -8.10754 | -55.07868 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17094b32-2a67-3835-8b3d-bc89b9ae03ba | -4.95825 | -45.07116 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2ef615d3-ae94-32cd-bbd3-019acc6dc63f | -6.46091 | -44.56975 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c06d2f67-f2c9-3d8b-8442-e3807f965eb6 | -7.70247 | -42.56837 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6b8495d4-b6d1-37e1-a2e1-a617e7a059c4 | -3.83972 | -44.55236 | 2025-10-04 05:04:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92af0165-1c08-3959-9ce0-7b651b673d29 | -8.20379 | -46.99421 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4408d0d2-3046-3952-8bed-9896a5f99512 | -8.89061 | -45.02654 | 2025-10-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 020e1e30-683c-37a4-902c-9a992d3bbad5 | -8.61955 | -54.99691 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c8fb7dd-2cf7-3c62-965f-e32d15852408 | -8.1256 | -50.23888 | 2025-10-04 05:04:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b4c9e3d-1b81-3378-b4de-8dd0f9b32940 | -4.89555 | -49.96389 | 2025-10-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc923ca7-9af9-3579-b32d-ca3f3d4ecbd8 | -9.94828 | -50.89223 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3b78bfe-242c-3e32-93ce-d84fce489044 | -4.44318 | -43.23992 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 9fb47d61-0662-3969-bb0a-62a6834628af | -6.37964 | -43.89412 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7db3e697-f852-3d9e-9d3b-954a6ff2fdc8 | -6.0769 | -42.51809 | 2025-10-04 05:04:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2bfe5e48-123a-3988-aada-09d4e59daf4e | -2.98624 | -48.75908 | 2025-10-04 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 768e23db-595e-365b-a505-03cdb2be5815 | -3.8256 | -51.91615 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91e21467-d657-3eee-8d56-2c40bab0d676 | -4.44311 | -43.24453 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 3ce2da4a-82ec-35ea-8ab0-3b5d45a61a28 | -7.72889 | -46.29977 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fac50a68-9fcc-3ba1-a5ef-cd5af19027d6 | -7.80546 | -42.53257 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3bd4dfec-fdd8-3cb4-b44a-7daea7e2c9fd | -6.66962 | -42.83344 | 2025-10-04 05:04:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e21d5959-608d-3879-90a6-63bcc4ef8c76 | -8.17008 | -44.13004 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87e58cd3-4976-328c-ba6a-21bcfa678062 | -7.80371 | -42.54646 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9973e525-a3a1-3d18-944a-cedd4b043781 | -8.62907 | -55.00202 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72ae222e-8ced-3f3f-9a56-2eda9022c570 | -6.88278 | -44.50269 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a2cfc7f4-ef30-3b81-87fd-7c74f1103e07 | -7.16192 | -44.9924 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb4d9ea2-ba16-3813-9a0d-17d6c74a143f | -6.38378 | -46.50627 | 2025-10-04 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 934b1bdc-edc5-3049-9322-a20340c9c337 | -8.54233 | -50.15465 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7212552b-e701-362c-82d9-dcd216d6c80c | -6.24737 | -44.24374 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 782fd321-b7ac-3837-99ba-c9909a87e6aa | -5.08517 | -44.09241 | 2025-10-04 05:04:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4da8690-92ac-3ec4-93f1-1bc1f74c8592 | -6.06998 | -42.51722 | 2025-10-04 05:04:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| dcbc6a79-53dc-3022-893d-bf440f30e47e | -6.43208 | -44.45641 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23b74bb0-1a9d-3275-a2ea-528a77f648ef | -2.78101 | -51.79501 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0f91ae4-0e73-36cc-94d6-9d701e865827 | -3.90687 | -52.16603 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a98f4b30-2b1c-3069-9a06-1a657d8fd951 | -9.42234 | -47.53086 | 2025-10-04 05:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 929a3610-1405-3f2b-8877-1f25d7997a3b | -7.77226 | -46.26173 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90125862-c324-33e5-9430-bc6a5f562860 | -5.49122 | -44.10734 | 2025-10-04 05:04:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0191fabe-db37-32dd-ac0c-15669fa4ec5e | -8.06304 | -44.79913 | 2025-10-04 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6572f97a-6f26-3525-b583-e2135f37368f | -6.66988 | -42.82001 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 631696a8-a4b5-3f95-b272-6b5c15d0dc21 | -8.6133 | -54.97023 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2f00f18-7346-365a-9ac0-706ace115a70 | -9.18039 | -47.69849 | 2025-10-04 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c58d171e-fb68-3403-992c-9c996768e53e | -4.44887 | -43.24641 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 7f567c6e-d661-34d8-8f15-a0187a6c6957 | -6.18592 | -43.59695 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 90e1801d-4f91-30af-a184-ec6a5ad270f1 | -7.85799 | -48.20331 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92b3736b-8d3a-3ee8-8200-624509d6f858 | -8.14265 | -54.85019 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 183d5f35-9a0a-3408-93c1-e7c4056da825 | -9.3168 | -54.53426 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b456d89a-5b68-3392-b0b7-1322139ee1bd | -8.82192 | -44.82129 | 2025-10-04 05:04:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95ccd1b3-01b1-37ff-8bff-52386b591234 | -5.71703 | -44.24178 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7c15cb7-7c5d-3174-9084-8060909f4cd4 | -9.33952 | -54.52543 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 556947ca-da49-33fd-a09e-2342501576a3 | -9.66673 | -48.22505 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6147343-367b-3ed2-a32e-ad5b3879ab11 | -6.93759 | -63.12386 | 2025-10-04 05:04:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28e363c0-f015-3516-b569-54bd3c30f65e | -8.62119 | -54.98616 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README107.md)
