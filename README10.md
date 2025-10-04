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
| ec353607-b5af-354c-abaa-63bf38020099 | -6.1782 | -43.927 | 2025-10-04 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d0c8be6-d9b1-3dc2-ba89-577a04636baf | -5.82826 | -42.88293 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5ce1b9f4-64c9-394e-b847-173787cb0309 | -9.89891 | -43.73812 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 320ef1d6-2de0-3b7f-b809-5f0daa337359 | -6.88421 | -44.50195 | 2025-10-04 03:23:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fbac2586-3a7e-3176-916e-bc3592f31fb1 | -9.11483 | -44.39408 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7abbda4e-edd0-3470-a6fa-bc8926e477af | -10.83482 | -41.27453 | 2025-10-04 03:23:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 134a218a-2079-3e3c-87fd-a5a6576f95c9 | -6.06248 | -42.51953 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| df69fea9-7513-3402-815f-ae95b42f9403 | -6.2672 | -42.45444 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 63c5d224-3c72-38c7-a26a-f035849b38a7 | -7.33245 | -41.43921 | 2025-10-04 03:23:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 29357ee5-e798-32d2-93d7-4b59b9f52d8f | -11.11655 | -44.89965 | 2025-10-04 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5800e2e4-6034-339c-81d2-9d209cf44456 | -7.71058 | -42.56769 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b2260495-6dc1-3fd1-8c56-df5890bacb98 | -7.7034 | -42.57143 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 02703ffc-8bfe-31c1-832a-10add10705d7 | -9.90499 | -43.74054 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5cfc2252-e9e2-3687-8991-ddd6f260f7fc | -6.05586 | -42.51095 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 16f9850d-0e2b-382c-937d-441425d04cf9 | -5.98358 | -43.48175 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c58ecdbb-7ff6-3516-b838-8368a077803f | -7.33166 | -41.44347 | 2025-10-04 03:23:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 67f7f226-a0f9-35f3-be14-64e31cd20ad5 | -11.45177 | -43.49649 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5d5243b-7e16-3210-a61a-a9fc1a48fefe | -11.15008 | -43.38607 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 97050f62-44ae-3489-b20d-8e3f53b6b418 | -6.67124 | -42.81598 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6ad298e9-e5cb-3b83-a164-a4ba4b8868ef | -7.73908 | -42.60933 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4c1a9b66-2692-3316-837c-9248cb0f23f6 | -8.17145 | -44.13339 | 2025-10-04 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 758a4404-e84a-3c65-b1c9-d02a5948db56 | -6.36772 | -43.90279 | 2025-10-04 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4f5f4653-a746-3bfb-b391-216406136dc6 | -9.91003 | -43.71626 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ad77f845-4abc-3bae-8f7b-507451e64148 | -6.27724 | -42.44758 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1493abac-f7d8-3483-aab4-1da1b2c95391 | -7.74112 | -42.59871 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2184ce11-393e-3948-93df-3858608342f6 | -7.76023 | -42.61448 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 114771f0-a3bd-36c7-8d6b-e7a904b8cd5a | -7.05312 | -42.7874 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a61de9b1-9daa-3ec5-abc9-a35e5b78c737 | -10.02517 | -44.01832 | 2025-10-04 03:23:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0996a6eb-6897-3fd7-9229-077a28395215 | -6.2781 | -44.04224 | 2025-10-04 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0b690e9f-1647-3bb4-8aac-b6ad221d84b2 | -9.91195 | -43.74019 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4d5aa5a7-6287-3993-bf06-944ce7eecbbc | -7.05144 | -42.78833 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 90675e86-fd15-31e4-8b23-3fdc79e17918 | -6.28377 | -44.05062 | 2025-10-04 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0adac2b5-7f3b-3bb5-ad11-18901a6464c5 | -9.90072 | -43.72796 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| cd0e98ca-91ea-3276-81ad-3aab9bdc3e1a | -5.9904 | -43.48283 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0b544a00-2687-3a2e-a86d-fcadfd473c28 | -9.94649 | -43.73546 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a43dfad-2bd7-3b64-9e05-d6be364694de | -9.65967 | -42.93731 | 2025-10-04 03:23:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8c74b454-5a48-3108-b46e-fc7e4011ff9e | -7.71593 | -42.57371 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1a64c53c-368f-307e-8140-eac995b35776 | -6.05487 | -42.51654 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e1e72cd3-f488-39dd-9bf3-c62e2d0fb45c | -7.74148 | -42.61066 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e04ccab6-0aed-3907-8642-b99191f06967 | -6.67234 | -44.20874 | 2025-10-04 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 417dd1a7-b131-37ac-af83-d37e0f78219a | -9.11361 | -44.39339 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ab6ef296-402a-3dc1-bfaa-3f3113ecba64 | -11.15231 | -43.38383 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2f89c8d-a37c-315f-aab3-7e7fe275b3a6 | -7.78854 | -42.49501 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 31be7a3a-9145-343e-924c-ba362d2cb46b | -6.06765 | -42.51906 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| eea21604-b8f9-36c4-adaf-ef629466c8ff | -6.07824 | -42.50581 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| cce61fa0-dccd-3c14-bd7a-31081f8791b9 | -7.7493 | -42.52237 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 9bfa0ac8-24e6-3304-8a8f-b279bd860cef | -6.87587 | -44.50733 | 2025-10-04 03:23:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5329e670-3c49-34cd-b27d-9525b0ca25bc | -7.7877 | -42.49963 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 25e0ea5a-1062-38f3-a56d-488e87ca0c04 | -6.72087 | -44.15191 | 2025-10-04 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c08fcfae-532b-3996-bc15-6fd5891a624d | -6.07631 | -42.51628 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 40bdc565-9cd9-3798-81f9-791f527ea21f | -7.75275 | -42.54955 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9d415a3a-3a36-36c0-af04-5aefb45017eb | -7.05413 | -42.78207 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bfe32ef9-3c7c-3525-8a10-767041b69ca4 | -11.15412 | -43.39793 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6bba769-2562-33f9-9267-2e541d0d505f | -9.10549 | -44.40532 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 62969936-5351-333a-981c-26a9b1d458e0 | -9.90542 | -43.73921 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9edad7a4-f079-3ae9-9b34-444ce5324a2a | -7.33301 | -41.44328 | 2025-10-04 03:23:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0b34f118-aea3-3e28-a0b2-793945e3909d | -6.35229 | -43.45134 | 2025-10-04 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4575a2cd-0247-3253-802b-c76a32fa188a | -6.22086 | -44.27224 | 2025-10-04 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb7a56ad-d87b-3e8b-828f-7102006195fd | -5.8369 | -42.87266 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 48e2ceb2-c97d-36e3-baf3-ba90f58d2d0b | -5.6884 | -42.84785 | 2025-10-04 03:23:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| af745449-a62d-3385-bf9e-67f78b9f7825 | -6.65367 | -42.8028 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7781eadb-5faf-3e69-9c92-1c1d4cf02f70 | -8.17712 | -44.14059 | 2025-10-04 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0ddb806b-761b-34d0-a9d3-135868dd2258 | -7.78476 | -44.14162 | 2025-10-04 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 381d7747-44a9-3e21-b46a-7674a0e26edc | -7.55248 | -42.39966 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fd2e0f9e-768f-3dc6-95bc-31f7452130a5 | -9.95293 | -43.73681 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 420a8042-a447-3e80-ac83-6ee4cfc5091f | -6.87352 | -44.50072 | 2025-10-04 03:23:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 786f20e8-4d9e-39e6-8036-28193154fa7a | -7.7574 | -42.52433 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ca8e3c3e-f589-3d33-bc3c-473c740e7813 | -9.9125 | -43.80479 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7973ee16-bb3a-3895-bb62-cf6eaea118ca | -6.07687 | -42.5043 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| c8ad645f-ac57-3588-b1ec-bbfa23f1773d | -7.77973 | -42.60025 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9e237ef5-0981-370f-aa3f-074eadee84b7 | -6.22677 | -42.93556 | 2025-10-04 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a80f732f-851a-3af7-b3b9-283eed3940d0 | -7.75018 | -42.52847 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 348c6a2c-e4ae-3406-8384-e4510b8d1850 | -11.12335 | -44.90092 | 2025-10-04 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7fda815-bd1f-32b5-a9cc-20fc5992f2b2 | -6.3691 | -43.8954 | 2025-10-04 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c985528d-c67f-3f19-98af-db5ea675e1e7 | -7.80366 | -42.54207 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ec03de3f-4740-3ecf-9ef9-cf31dd0d6fad | -6.71086 | -42.8183 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98c675b4-d03f-3b2d-b37e-648649b9f34a | -5.95894 | -43.49294 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5a91d1b-9c8e-337d-a674-d8330cd9e2b4 | -6.17117 | -43.92617 | 2025-10-04 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d93c2ea-8da4-36b4-93e5-2199162f4a84 | -7.56583 | -42.62803 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3093b77a-8ccc-3851-8f5a-835867a3cee3 | -11.44555 | -43.49526 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ba9c385-2527-3fa2-992c-a898c700443f | -9.91356 | -43.8007 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e8c623e-7866-3d22-afc6-04c50cffb49b | -9.91362 | -43.79919 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bc4a759-d014-3c82-a4ac-e7c68e9fcb22 | -6.69423 | -42.83606 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c317f36-824f-30c8-bbae-cff4fa627974 | -5.9885 | -43.48463 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 304575d6-4bf3-3415-a62f-78d6d9e0ed89 | -11.42986 | -43.48526 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 132d914d-7708-3347-bd2a-bdfbc35d518a | -7.55867 | -42.39301 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 24564993-6ced-3127-9a52-7f6fa1609e7f | -7.55863 | -42.63168 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b9e8baf0-ecc6-3048-8490-a72d38dd3c2e | -5.73734 | -42.93328 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 58b889e7-70db-3003-86cb-34de59ebfe45 | -5.48928 | -44.11228 | 2025-10-04 03:23:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5223ccf0-0cb8-3e28-8ff7-74e7f12ed37d | -7.79228 | -42.49988 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d08754b4-1c6c-30d4-b4fa-0b4445cb2454 | -7.047 | -42.77649 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c5f07ee4-c164-30ec-a5e7-1b47df26b39c | -11.44035 | -43.4975 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 814c0565-7e26-3e24-a819-ea7074fef2d3 | -7.79554 | -42.55086 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9471ede9-30d3-3fc1-ba8e-210df3542455 | -8.06103 | -44.80013 | 2025-10-04 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9de2c853-a846-339e-b2d4-6b47018a0563 | -6.07092 | -42.50966 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 3fffedb1-9e2f-307d-ad39-b41dec057c2b | -9.91151 | -43.74158 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 825bb5c4-a86b-3c33-9825-0716edcd5686 | -9.10688 | -44.3984 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c5b694f-bad8-3979-b3f5-ef8f1de07363 | -6.17241 | -43.91949 | 2025-10-04 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 417ed017-4515-3c50-9e05-cca3beb8af93 | -11.42267 | -43.48894 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97b80aee-2dc7-3d6d-9894-6a37e72c62dc | -7.71404 | -42.58385 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README11.md)
