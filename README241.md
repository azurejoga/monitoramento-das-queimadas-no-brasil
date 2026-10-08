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

## Dados Diários - Página 241

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0570661-43f5-3fee-aa45-6272e240c149 | -6.95548 | -44.41986 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 52d5c310-9a09-31bf-b413-6beb1f81eb9d | -6.49572 | -41.82825 | 2026-10-08 15:41:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 96fd5637-ac2b-3147-a676-01aee0a0addf | -10.0412 | -45.60078 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7f271681-03b7-32fb-b951-ec4d8c5e032c | -6.35725 | -42.91264 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c6ebdfda-a2e7-3e24-b2a0-39ed687f94a4 | -10.38162 | -46.29977 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 879ed7ba-fbc2-3c5e-ae97-f10815d0c576 | -8.93723 | -45.16729 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 87005fb1-e199-306a-86d3-1fd802c95205 | -7.25249 | -39.40807 | 2026-10-08 15:41:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b6c76ab1-0293-334b-88f8-ee3b04abb2ae | -4.75166 | -40.92418 | 2026-10-08 15:41:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| af62e6a3-bdd0-3410-9735-8fac30428ab4 | -11.2673 | -45.19574 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3fe952bb-b388-3783-a5c9-0253ca31f585 | -7.53552 | -45.8786 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| dc0e9ff4-ff3a-3929-a2ba-6a83a77dbd14 | -11.00259 | -45.41937 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 72026829-0802-362a-80b0-7a844cbe8f8d | -6.37555 | -42.52768 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| fe4de5e2-548c-366c-ae92-2b9a4af87a15 | -7.2519 | -39.40382 | 2026-10-08 15:41:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3a638cbb-c12d-3137-9620-fcbd67e14671 | -10.15995 | -44.67177 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 11006ea1-ada2-3e17-8f23-ff7925a80b1d | -6.32872 | -43.83499 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 61b74701-e3e8-3e30-9d76-598b0332d585 | -5.77332 | -42.05338 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 6c1b29b0-0899-3534-b8b4-0c2d4f9a11d9 | -7.05063 | -44.34088 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 453f05ef-913f-326d-aff8-e6d3faec940a | -5.73039 | -45.16476 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fb9bcd55-b327-3833-ab09-99ad80c01bd8 | -6.6371 | -44.89432 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a240731d-f6dd-350c-a2a0-73d4b004a80d | -6.05996 | -42.92139 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 88237a8d-995a-310b-9d0e-a33a14f06752 | -5.30334 | -45.72386 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| c068dccb-b4b2-3c4f-b6f7-56d043852419 | -5.36132 | -43.20315 | 2026-10-08 15:41:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afb5c427-e9a9-30bb-87f3-46cc551b6935 | -6.96382 | -45.26168 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a14a0828-a2ff-35b4-a625-a313b3d04af9 | -5.29039 | -42.74291 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 2572c4f2-4d4f-3cda-8e25-b4cb275a347e | -7.11238 | -42.53664 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 47057a8f-c5c9-351d-80ea-b28ee453435b | -8.94035 | -45.18193 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 6f420864-8efa-3550-a5db-b05f0b306d48 | -5.95844 | -40.94934 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 14b5f84c-a125-3d5c-8433-0e7aff51d774 | -4.26327 | -38.72746 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 212106d2-8049-398f-82e3-789fec316e8e | -6.84963 | -39.54841 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 50d3ee5c-104a-3066-93a8-38c24c9ba0b6 | -8.93892 | -45.1706 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 326.3 |
| f063c256-a9f9-35c9-b949-7c42b24156b1 | -6.68559 | -41.76287 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 5e831423-b8fa-3745-9f51-eb283ec6db17 | -6.32826 | -43.83455 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ac6c4f8f-7968-37e8-af19-9a44a900d425 | -4.30329 | -38.10372 | 2026-10-08 15:41:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 31632f23-1aae-3283-bbcb-10bcf63cd926 | -4.5815 | -40.64827 | 2026-10-08 15:41:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8f8459c3-841c-3b88-b660-367071d073cb | -7.47425 | -42.85306 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| b5a4de97-4e73-3e99-b39d-842d6cea966e | -8.29882 | -44.1741 | 2026-10-08 15:41:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 01359e08-4479-34cd-83de-2b9eb69402b4 | -7.59772 | -42.38821 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| aa42d1c1-fd81-3534-a342-263e4d7934b7 | -10.22278 | -40.04269 | 2026-10-08 15:41:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f7a37e4e-59cf-3701-a62c-eaa73c8fc912 | -10.95938 | -45.39098 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 232a3abf-1328-352f-a098-e4037d1fce14 | -6.33458 | -35.15139 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 2e1f5a14-6d41-3062-aa6a-d4f5c6ee0eee | -5.71109 | -41.67426 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f3949376-3851-381f-8722-4169f488def8 | -6.17082 | -44.85862 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| f58f5637-6c56-3fdc-8554-7aa440869079 | -9.9342 | -43.57299 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 6189fc49-d572-3521-a1b4-d8bf2b2ecc8e | -9.07763 | -45.11585 | 2026-10-08 15:41:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ebad0419-3ff9-380e-ac86-cc06e0775ef5 | -7.31532 | -44.54199 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 148b7c8c-7523-36c9-9c5b-4f8556ef84e4 | -5.6268 | -43.04596 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 067888b4-62bf-34b2-9b18-6859ec71f5f1 | -7.41196 | -43.7458 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e277c49a-34b0-3231-bc22-c0e29f2873e7 | -7.66315 | -45.38766 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 31b67257-b558-3af0-8486-c53d7377bc87 | -5.74232 | -42.0723 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 81238d40-6815-33e8-8436-579ba633ac6f | -6.93845 | -41.9493 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 99905804-923f-3988-8dd1-bef1df596271 | -9.02897 | -44.36221 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| d1c05cd6-d62a-3eae-9728-21717e6c818a | -9.44414 | -44.60226 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e0c35255-26a5-3f3b-827c-4a779d7f90ac | -6.509 | -42.03233 | 2026-10-08 15:41:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| df4c72a8-2111-308e-9dcf-3217ca327ffe | -9.8973 | -45.19371 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 10d1151b-ddff-31d7-a230-d6be8e43f59e | -11.11343 | -45.70444 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8e43dc46-c0be-32f0-9e0b-a5b5895e0aa1 | -8.87952 | -41.44857 | 2026-10-08 15:41:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 76c09733-dde8-31b6-abc8-bd14b3462d2d | -7.20114 | -44.29307 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2a20414a-83e2-3c94-9d8a-ba609c11fc3d | -9.5533 | -45.64038 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 354f2a7e-da5b-3d5c-81cf-cbff2830f329 | -5.43709 | -45.68489 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b3d558ac-5c73-3fa4-b273-5839345d3a1f | -5.95888 | -43.90494 | 2026-10-08 15:41:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bbb513ef-a075-31ed-8673-3c92bcb0260c | -5.74779 | -41.68101 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6449eb4f-a619-3a90-b1b5-c2f9a2e88ca3 | -7.05584 | -44.32609 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 941baf92-9d43-3b8b-b8d6-8c54f6cf733b | -8.06879 | -45.62202 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a6c8622d-cefa-3d8a-b1c1-23c7714cb1a5 | -5.51103 | -42.82605 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| d5d841af-e9e4-3121-be53-5bb4e29bdfd4 | -6.23642 | -43.85678 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5aeb748f-b4d4-3b3b-b25c-8cbb1b903a67 | -7.09691 | -44.03484 | 2026-10-08 15:41:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc54eb2f-8ddc-3bc9-8be6-1b13780afb60 | -5.37719 | -44.64308 | 2026-10-08 15:41:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 56747afc-ee52-3336-ad74-e032fa78a50e | -6.53534 | -45.3771 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 3cbbd81f-09d1-3951-bc92-58a55aeb3bd7 | -9.97637 | -43.50019 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2fc8f6dc-6131-3059-b618-3a5116965758 | -7.21545 | -44.15425 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c5644a28-e3bc-395e-919f-932be098c3cd | -8.94518 | -45.17792 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bfa6bb1c-b841-3e52-8aa2-0ba1dbea3661 | -8.09984 | -39.8843 | 2026-10-08 15:41:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 24fe51d2-6c7b-3d09-a82b-efe0848d9c79 | -6.57067 | -41.60649 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c119eaa3-0812-31eb-8d30-9ba2d14422ce | -5.10773 | -43.16271 | 2026-10-08 15:41:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 65bbc387-48cf-3910-859a-382590b6e5c3 | -5.30406 | -45.7293 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 55b08eee-a555-3844-b3b0-8ae168d90bea | -5.71276 | -41.72129 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 97c61b27-492f-3818-80d7-0425d17d6c0d | -5.73467 | -41.76611 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 887c7af0-75a1-3beb-bd33-ea25fc6b43a5 | -6.57108 | -41.60948 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c99b584f-01f2-3ec1-bc7a-d0dd19deb738 | -5.73597 | -45.15861 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4b05a596-f90b-370c-a0e6-a942b421a160 | -7.31697 | -43.99634 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8adddbc-9c12-3c6b-8463-25b0a705da3a | -9.94132 | -43.5632 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f2a1a1bf-adab-35e5-9506-cb9cfc05c20a | -9.04467 | -46.60213 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4c78fddf-f300-30c2-a4aa-f2886e000e85 | -5.71238 | -41.75423 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 04c2c816-d167-333f-9867-908730f2c713 | -10.98113 | -45.40003 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 82c571d8-e099-387c-a8db-727276dcc095 | -5.48689 | -43.96533 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 397d6294-3662-394a-92b9-457941334367 | -6.2303 | -35.34517 | 2026-10-08 15:41:00 | NOAA-21 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 94d71a4f-3bc1-3780-bc5f-09271f16a770 | -7.46405 | -42.85592 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6ff39fde-1bcd-3d21-8def-5b5378f143ee | -6.05232 | -42.59231 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 262fe814-fd92-32be-b235-a316f5e09987 | -9.77383 | -45.88911 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 4e78d24d-3c5f-3545-9dbf-a0ff6c9c2c19 | -6.05328 | -42.59906 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 75f47809-3ebd-3680-a83c-50dbf2e0a181 | -6.66516 | -45.35717 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 94771304-3f80-3d0e-908d-c2a7c4e3d3e5 | -8.95425 | -45.14236 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 810d4515-7ea3-390e-894e-394d23b8df87 | -6.38898 | -44.94336 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bacde37d-dd8b-3562-af1c-d7d0c77bdab8 | -5.90987 | -35.38174 | 2026-10-08 15:41:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 4fb630f4-4b45-33d9-b1ce-850a837de6d3 | -8.95721 | -45.15687 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 87096144-ed84-3f21-b07f-c9706bbe664b | -6.94779 | -45.28106 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2815abbf-c3ee-3965-ae84-9a405f8e382c | -9.51465 | -45.60704 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 8a43aca0-33c2-3d3a-b8c0-9eb5b0f4fdc4 | -8.95038 | -45.16559 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8fca50c2-4ec0-31fa-8e46-277c2d330069 | -7.68587 | -44.74647 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9acd366-0ec3-37e1-80a9-3fd0ea06a437 | -6.81456 | -38.53239 | 2026-10-08 15:41:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |


[Clique aqui para ver as próximas entradas](README242.md)
