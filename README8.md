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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd2af8c-fb89-340b-baae-14a686e34882 | -7.20001 | -43.19373 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8db0b34b-51d4-3281-b510-db7dc9741ca8 | -7.21909 | -43.08834 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 0372a38d-9169-3f89-bf9c-c128bc9e0610 | -7.55276 | -45.83501 | 2025-06-27 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 210cee68-96fb-3e85-b0da-eff92dfd5a52 | -6.27021 | -43.68305 | 2025-06-27 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 47ca089b-cfcf-37bb-a9b7-a066f3c9db10 | -7.55149 | -45.8417 | 2025-06-27 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 947aa7b5-3191-3df2-a3ae-41b9940d1404 | -6.95864 | -42.90326 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| cc33961f-ba65-3b5d-b6e4-b3934cdbbc76 | -6.27329 | -43.67944 | 2025-06-27 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1d10f153-2d1e-3d55-bff9-a357d3527997 | -6.95534 | -42.89679 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 14815571-3ddd-3b45-934f-fa5bdb58d9b0 | -6.22208 | -43.36446 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88c8a9fe-ec6f-30e6-840e-5f3486215dca | -5.85163 | -43.6418 | 2025-06-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 295ae29d-4a42-372b-aef7-a0d7defa1c91 | -9.7866 | -36.99744 | 2025-06-27 03:28:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc56cfcd-257c-31e4-982d-8e8316017f28 | -6.95357 | -42.8979 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 48a40c96-fc6d-33cd-9b7b-c9aa502bb9d4 | -7.21316 | -43.08729 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| c4a210fa-146c-3e17-86d0-21c4a3b99279 | -6.47482 | -43.75057 | 2025-06-27 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b533c367-fa4c-3ae5-b7d8-b1bf8f491439 | -6.94929 | -42.88825 | 2025-06-27 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81527585-ac1b-37bf-84c4-c5af56d7bfd6 | -11.5776 | -52.136 | 2025-06-27 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 85343762-f2f8-3805-8804-99e9f665b8e0 | -11.5779 | -52.115 | 2025-06-27 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 440.4 |
| 7960b1a6-d78b-3cb0-a239-70f187d17717 | -6.9602 | -42.9052 | 2025-06-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 321.7 |
| 7f07c13d-6a60-3d5f-96fe-c6bd073566f5 | -6.9416 | -42.8834 | 2025-06-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 687e7a10-7e57-37fd-930a-443cd82f617d | -11.5969 | -52.113 | 2025-06-27 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8e7e6bf6-51ee-3900-bb9b-f3e853a32c9d | -6.1789 | -48.0929 | 2025-06-27 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 1f83a334-d8ce-3be5-8aa2-f2d86fe87252 | -11.5782 | -52.094 | 2025-06-27 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| b98a5316-9cbd-352e-9d2a-558ef3426f0d | -6.9414 | -42.907 | 2025-06-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 7a6acec9-fbb7-3760-82bd-1100d13a6cd9 | -6.9791 | -42.9034 | 2025-06-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 168.0 |
| 8a05f98e-f7c0-306f-83ac-bb7a1552bd84 | -11.559 | -52.117 | 2025-06-27 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 3cd1de27-861a-307d-a1ba-eb3fdbeb799f | -6.9793 | -42.8798 | 2025-06-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 156.4 |
| 1d6e2b5a-03b1-3757-80f1-89d8e35824f8 | -6.9605 | -42.8816 | 2025-06-27 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 302.9 |
| 2ff74c04-e9ac-3ea4-a57f-56ec2d1e9882 | -12.43098 | -43.72172 | 2025-06-27 03:30:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0fb6222f-8064-3b9d-bc9a-ff9e07291b52 | -12.74947 | -44.40985 | 2025-06-27 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0585d8b6-4dbd-3acd-a718-e98efa8390a0 | -13.58027 | -45.25848 | 2025-06-27 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88c9678a-28f2-3576-ac6a-fa30b9da3814 | -10.62265 | -46.70771 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3e79944c-8ccc-3ff6-b95c-a097eaaf605c | -13.58634 | -45.25972 | 2025-06-27 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28a1e65a-c8db-3b0f-bd2a-c71005f6bc89 | -13.6458 | -46.81116 | 2025-06-27 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33c76823-4ee5-3f38-9cba-cdc674643d7f | -11.81 | -47.52719 | 2025-06-27 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6000a5fe-5353-3f98-a922-cf54ca639a8a | -10.62125 | -46.71444 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eb35fc2d-c10e-399c-846a-05a0f36e7352 | -11.81898 | -47.53535 | 2025-06-27 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d696088d-b0e2-383f-bcb9-31d653255087 | -11.58454 | -44.64588 | 2025-06-27 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa9e4470-214a-33bf-b599-b8fe54951e41 | -11.80268 | -47.52671 | 2025-06-27 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 631ac619-b545-39e5-a45d-24f871f5def5 | -10.62788 | -46.68829 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a694d5c3-85dc-339f-8bde-750b38a66553 | -11.81225 | -47.53211 | 2025-06-27 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6aa8376e-fe3e-35b8-b64d-77e0982f1bd2 | -14.20907 | -45.50626 | 2025-06-27 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 926eacec-2c67-3ac0-894a-e44122ca66ef | -12.00916 | -47.15989 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dcd1a8a-6741-3da0-9fa6-7eff92c105b0 | -10.65 | -44.49633 | 2025-06-27 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b99b63ce-2340-3f99-99d2-2f1c20fb053e | -12.76201 | -44.408 | 2025-06-27 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c191215d-19ff-328a-b03c-b6f6ca76ae3f | -14.2086 | -45.50959 | 2025-06-27 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50524eea-25a4-3f3f-a6cf-cec7281dd214 | -10.63367 | -46.68949 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 001a4f87-84aa-3d3d-89d5-24343b1e2e2f | -12.00067 | -47.15791 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c451a501-ba8c-3da2-ac2b-a88197954b16 | -11.68398 | -46.73086 | 2025-06-27 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09eb144d-5a7b-3374-bfb4-a47af34795f0 | -10.62653 | -46.69497 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b6d9c320-3072-3144-8689-30b18abef90c | -11.99922 | -47.16461 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8ebe802-192f-3197-9ae7-e70a89ca4746 | -10.62384 | -46.70834 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 251d70b7-5158-3ccf-9533-89d2c70d4845 | -11.81353 | -47.52621 | 2025-06-27 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b50280a-9eb8-3e83-8964-7c613c342da4 | -14.20203 | -45.50962 | 2025-06-27 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d24cdb4a-a6af-3f72-889d-3a2726a72e1a | -12.75444 | -44.41538 | 2025-06-27 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6158bc45-642c-31a5-bd28-467a5e940ec6 | -10.62954 | -46.70935 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b14cabd4-1919-3d0e-82d1-0949ad27029f | -11.58586 | -44.67047 | 2025-06-27 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b961999e-eb95-3350-9166-6f0db73be1d6 | -11.8154 | -47.53682 | 2025-06-27 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a57045e-a617-31ee-856f-b222e4238527 | -11.83794 | -43.79895 | 2025-06-27 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 45342635-7582-3e2a-b6d2-7c436994b684 | -14.2081 | -45.511 | 2025-06-27 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ddb71ea-53be-3573-86ca-3ed40ac421ce | -11.99385 | -47.16372 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2141b222-be1b-3022-823b-27434852cab4 | -11.66903 | -46.7342 | 2025-06-27 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b572703-18ac-35f2-94be-0f81336a4d05 | -14.09653 | -41.87341 | 2025-06-27 03:30:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd7ad71e-9b41-3cde-9087-59ed39c29d8d | -10.62681 | -46.68773 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d55bfbe-c133-3021-885e-b974948c130d | -13.16037 | -45.23112 | 2025-06-27 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d4c2775-28ef-3f31-9019-6b296a012b61 | -12.00618 | -47.16602 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a32d153-78bc-3b09-85d7-ea1485f08c3b | -12.00221 | -47.15846 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab395e54-9b84-35e8-aabd-05340b1e9bda | -12.75531 | -44.41107 | 2025-06-27 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e7bba6ef-af63-3723-8721-41786c71ac8e | -10.65056 | -44.49332 | 2025-06-27 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 00005219-78b0-3aa7-981a-eae85a4998b8 | -12.74861 | -44.41415 | 2025-06-27 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 517a9199-6636-3563-9229-ff140e1e1d56 | -12.00775 | -47.16661 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2590947-c7ee-3f27-8d6f-e14ace787f15 | -11.817 | -47.5292 | 2025-06-27 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a1693f1-003c-3cdf-a2d0-742dc1c60db7 | -11.58938 | -44.64842 | 2025-06-27 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 932d47e8-7880-3e20-8b67-67599a4a3f4e | -10.62543 | -46.69437 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| af30dcc9-96aa-3adb-93f4-0c1b5f136892 | -11.58425 | -44.64247 | 2025-06-27 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6990d7d-93b6-3473-876f-b965de03faf4 | -11.99527 | -47.15693 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bca8f73-6a6b-37ba-b0e4-49e517383d37 | -10.62249 | -46.71505 | 2025-06-27 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 92db8d5f-72d3-3d61-a9a7-29b1205bdc22 | -12.00762 | -47.15934 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b10b292-9765-357d-a7bc-833d46ae9342 | -12.0008 | -47.16515 | 2025-06-27 03:30:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0d2d6f6-e614-380f-b1cb-c7a4ec14f96f | -10.65148 | -44.48867 | 2025-06-27 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b4d91d30-a1f8-3573-a9d6-6eb86d239812 | -12.76287 | -44.4037 | 2025-06-27 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c05f0fdc-0bbe-3a6d-8cc1-cd04fd8ef993 | -12.4302 | -43.72564 | 2025-06-27 03:30:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 724bda70-60f4-36ff-8d27-619f46b37f17 | -13.5793 | -45.26321 | 2025-06-27 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a6ac2f-353f-3012-a0d1-89f1ce0abbd4 | -10.6509 | -44.49165 | 2025-06-27 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6836b9ad-fd59-3a3d-9128-fc6908f3618d | -10.6946 | -37.04842 | 2025-06-27 03:30:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d31d74b3-95d4-34a0-8c48-be2e773dd1fc | -14.20759 | -45.51434 | 2025-06-27 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb99decb-67a5-363b-82b9-06a9f3482205 | -11.67725 | -46.72903 | 2025-06-27 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82060f96-6e9e-3fa4-a819-ea8aac8a283f | -11.83923 | -43.79762 | 2025-06-27 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d924cd1b-84fa-37dd-82b1-3b3132e225b0 | -11.58547 | -44.64125 | 2025-06-27 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 192694ee-b9b5-3e46-a56f-694148e165b0 | -17.04135 | -45.88715 | 2025-06-27 03:32:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4964774-7e55-3ce7-bad6-68314d55da76 | -18.75 | -40.07719 | 2025-06-27 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 604b27e0-9e35-37d2-aefe-ed2a192cca4f | -22.67514 | -42.85452 | 2025-06-27 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3bcb9058-cbab-36aa-9274-538b9edb159a | -19.45135 | -44.31375 | 2025-06-27 03:32:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 662c5fa7-4be3-3b2d-b0d8-e27bc11b138e | -18.75066 | -40.07357 | 2025-06-27 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f8622eb3-7aee-3270-8555-efd192067b05 | -19.45649 | -44.31479 | 2025-06-27 03:32:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f247a8a0-251e-3444-8da4-4ff6db74d2f0 | -21.66889 | -41.20849 | 2025-06-27 03:32:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 25936940-353b-38b5-8b0d-8a4b1e74a9de | -17.04372 | -45.89029 | 2025-06-27 03:32:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccdd3ef7-7575-3191-a494-fc018eae377f | -16.24885 | -46.29749 | 2025-06-27 03:32:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6fb82885-ba59-3911-9e5e-5f9586c1a5dd | -20.90854 | -44.12289 | 2025-06-27 03:32:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5114e211-7fc4-36e0-94e8-10fcd5aa2c33 | -17.0462 | -45.89325 | 2025-06-27 03:32:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d066d8f-3e4a-33d1-8518-00da7593caf8 | -16.67847 | -43.88499 | 2025-06-27 03:32:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
